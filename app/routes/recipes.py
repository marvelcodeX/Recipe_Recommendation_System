from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app import get_db

recipes_bp = Blueprint('recipes', __name__)

RECIPES_PER_PAGE = 12


@recipes_bp.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    db = get_db()
    recipes = db.execute("""
        SELECT r.id, r.title, r.description,
               COALESCE(AVG(rt.rating), r.rating) AS avg_rating,
               COUNT(rt.rating) AS rating_count
        FROM recipes r
        LEFT JOIN ratings rt ON r.id = rt.recipe_id
        GROUP BY r.id
        ORDER BY r.created_at DESC LIMIT 6
    """).fetchall()

    ingredients = db.execute("SELECT id, name, category FROM ingredients ORDER BY category, name").fetchall()
    categorized = {}
    for ing in ingredients:
        cat = ing['category']
        if cat not in categorized:
            categorized[cat] = []
        categorized[cat].append({'id': ing['id'], 'name': ing['name']})

    return render_template('homepage.html', recipes=recipes, ingredients=categorized)


@recipes_bp.route('/recipes')
def recipes_list():
    db = get_db()
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('q', '').strip()

    if search_query:
        total = db.execute("SELECT COUNT(*) FROM recipes WHERE title LIKE ?",
                           (f'%{search_query}%',)).fetchone()[0]
        recipes = db.execute("""
            SELECT r.id, r.title, r.description,
                   COALESCE(AVG(rt.rating), r.rating) AS avg_rating
            FROM recipes r
            LEFT JOIN ratings rt ON r.id = rt.recipe_id
            WHERE r.title LIKE ?
            GROUP BY r.id
            ORDER BY r.created_at DESC
            LIMIT ? OFFSET ?
        """, (f'%{search_query}%', RECIPES_PER_PAGE, (page - 1) * RECIPES_PER_PAGE)).fetchall()
    else:
        total = db.execute("SELECT COUNT(*) FROM recipes").fetchone()[0]
        recipes = db.execute("""
            SELECT r.id, r.title, r.description,
                   COALESCE(AVG(rt.rating), r.rating) AS avg_rating
            FROM recipes r
            LEFT JOIN ratings rt ON r.id = rt.recipe_id
            GROUP BY r.id
            ORDER BY r.created_at DESC
            LIMIT ? OFFSET ?
        """, (RECIPES_PER_PAGE, (page - 1) * RECIPES_PER_PAGE)).fetchall()

    total_pages = (total + RECIPES_PER_PAGE - 1) // RECIPES_PER_PAGE
    return render_template('recipes.html', recipes=recipes, page=page,
                           total_pages=total_pages, search_query=search_query)


@recipes_bp.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    db = get_db()
    recipe = db.execute("""
        SELECT r.id, r.title, r.description, r.steps, r.created_by,
               COALESCE(AVG(rt.rating), r.rating) AS avg_rating,
               COUNT(rt.rating) AS rating_count
        FROM recipes r
        LEFT JOIN ratings rt ON r.id = rt.recipe_id
        WHERE r.id = ?
        GROUP BY r.id
    """, (recipe_id,)).fetchone()

    ingredients = db.execute("""
        SELECT i.name, ri.quantity, i.category
        FROM recipe_ingredients ri
        JOIN ingredients i ON ri.ingredient_id = i.id
        WHERE ri.recipe_id = ?
        ORDER BY i.category, i.name
    """, (recipe_id,)).fetchall()

    # Similar recipes: share the most ingredients
    similar = db.execute("""
        SELECT r.id, r.title, COALESCE(AVG(rt.rating), r.rating) AS avg_rating,
               COUNT(DISTINCT ri2.ingredient_id) AS shared_count
        FROM recipes r
        JOIN recipe_ingredients ri2 ON r.id = ri2.recipe_id
        LEFT JOIN ratings rt ON r.id = rt.recipe_id
        WHERE ri2.ingredient_id IN (
            SELECT ingredient_id FROM recipe_ingredients WHERE recipe_id = ?
        ) AND r.id != ?
        GROUP BY r.id
        ORDER BY shared_count DESC
        LIMIT 4
    """, (recipe_id, recipe_id)).fetchall()

    # Check if user has favorited/rated this recipe
    is_favorited = False
    user_rating = 0
    if session.get('user_id'):
        fav = db.execute("SELECT id FROM favorites WHERE user_id = ? AND recipe_id = ?",
                         (session['user_id'], recipe_id)).fetchone()
        is_favorited = fav is not None
        rt = db.execute("SELECT rating FROM ratings WHERE user_id = ? AND recipe_id = ?",
                        (session['user_id'], recipe_id)).fetchone()
        user_rating = rt['rating'] if rt else 0

    return render_template('view_recipe.html', recipe=recipe, ingredients=ingredients,
                           similar=similar, is_favorited=is_favorited, user_rating=user_rating)


@recipes_bp.route('/find_recipe', methods=['POST'])
def find_recipe():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    vegetables = request.form.getlist('vegetables')
    dairy = request.form.getlist('dairy')
    protein = request.form.getlist('protein')
    spices = request.form.getlist('spices')
    grains = request.form.getlist('grains')
    others = request.form.getlist('others')

    ingredients_from_form = vegetables + dairy + protein + spices + grains + others
    ingredients_from_form = [ingredient.strip() for ingredient in ingredients_from_form if ingredient.strip()]

    user_id = session['user_id']
    ingredients_input = ', '.join(ingredients_from_form)

    db = get_db()
    db.execute("INSERT INTO search_logs (user_id, ingredients_input) VALUES (?, ?)",
               (user_id, ingredients_input))
    db.commit()

    # Look up ingredient IDs
    ingredient_ids = []
    categories = ['vegetable', 'dairy', 'protein', 'spice', 'grain', 'other']
    for category, items in zip(categories, [vegetables, dairy, protein, spices, grains, others]):
        for item in items:
            ingredient = db.execute("SELECT id FROM ingredients WHERE name = ? AND category = ?",
                                    (item, category)).fetchone()
            if ingredient:
                ingredient_ids.append(ingredient['id'])

    if not ingredient_ids:
        flash("No recipe found with the selected ingredients. Try a different combination!")
        return redirect(url_for('recipes.recipes_list'))

    # Find recipes where ALL recipe ingredients are in user's selected set
    placeholders = ', '.join(['?'] * len(ingredient_ids))
    query = f"""
        SELECT r.id, r.title, r.description,
               COALESCE(AVG(rt.rating), r.rating) AS avg_rating,
               COUNT(DISTINCT ri.ingredient_id) AS total_ingredients,
               SUM(CASE WHEN ri.ingredient_id IN ({placeholders}) THEN 1 ELSE 0 END) AS matched
        FROM recipes r
        JOIN recipe_ingredients ri ON r.id = ri.recipe_id
        LEFT JOIN ratings rt ON r.id = rt.recipe_id
        GROUP BY r.id
        HAVING matched = COUNT(DISTINCT ri.ingredient_id)
        ORDER BY total_ingredients DESC
    """
    recipes = db.execute(query, tuple(ingredient_ids)).fetchall()

    if not recipes:
        flash("No recipe found with the selected ingredients. Try a different combination!")
        return redirect(url_for('recipes.recipes_list'))

    return render_template('search_results.html', recipes=recipes,
                           selected_ingredients=ingredients_from_form)


@recipes_bp.route('/submit', methods=['GET', 'POST'])
def submit():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    db = get_db()
    ingredients_from_db = db.execute("SELECT id, name, category FROM ingredients ORDER BY category, name").fetchall()

    categorized_ingredients = {'vegetable': [], 'dairy': [], 'protein': [], 'spice': [], 'grain': [], 'other': []}
    for ing in ingredients_from_db:
        cat = ing['category'] if ing['category'] in categorized_ingredients else 'other'
        categorized_ingredients[cat].append({'id': ing['id'], 'name': ing['name']})

    if request.method == 'POST':
        title = request.form['name']
        description = request.form.get('description', 'No description provided.')
        instructions = request.form['instructions']
        user_id = session['user_id']

        cursor = db.execute("INSERT INTO recipes (title, description, steps, created_by) VALUES (?, ?, ?, ?)",
                            (title, description, instructions, user_id))
        recipe_id = cursor.lastrowid

        categories_map = {
            'vegetables': 'vegetable', 'dairy': 'dairy', 'proteins': 'protein',
            'spices': 'spice', 'grains': 'grain', 'others': 'other'
        }

        for category_form_name, category_db_name in categories_map.items():
            selected_ingredients_ids = request.form.getlist(category_form_name)

            for ing_id in selected_ingredients_ids:
                quantity_key = f'quantity_{ing_id}'
                quantity = request.form.get(quantity_key, '')
                db.execute("INSERT OR IGNORE INTO recipe_ingredients (recipe_id, ingredient_id, quantity) VALUES (?, ?, ?)",
                           (recipe_id, int(ing_id), quantity))

            new_ingredient_name = request.form.get(f'new_{category_db_name}')
            new_ingredient_quantity = request.form.get(f'new_quantity_{category_db_name}', '')

            if new_ingredient_name and new_ingredient_name.strip():
                existing_ingredient = db.execute("SELECT id FROM ingredients WHERE name = ? AND category = ?",
                                                 (new_ingredient_name.strip(), category_db_name)).fetchone()
                if not existing_ingredient:
                    cur = db.execute("INSERT INTO ingredients (name, category) VALUES (?, ?)",
                                     (new_ingredient_name.strip(), category_db_name))
                    new_ingredient_id = cur.lastrowid
                else:
                    new_ingredient_id = existing_ingredient['id']

                db.execute("INSERT OR IGNORE INTO recipe_ingredients (recipe_id, ingredient_id, quantity) VALUES (?, ?, ?)",
                           (recipe_id, new_ingredient_id, new_ingredient_quantity))

        db.commit()
        flash("Recipe submitted successfully!")
        return redirect(url_for('recipes.view_recipe', recipe_id=recipe_id))

    return render_template('submit.html', ingredients=categorized_ingredients)


@recipes_bp.route('/recipe/<int:recipe_id>/delete', methods=['POST'])
def delete_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    db = get_db()
    recipe = db.execute("SELECT created_by FROM recipes WHERE id = ?", (recipe_id,)).fetchone()
    if not recipe or recipe['created_by'] != session['user_id']:
        flash("You can only delete recipes you created.")
        return redirect(url_for('recipes.recipes_list'))

    db.execute("DELETE FROM recipes WHERE id = ? AND created_by = ?",
               (recipe_id, session['user_id']))
    db.commit()
    flash("Recipe deleted successfully.")
    return redirect(url_for('recipes.recipes_list'))


@recipes_bp.route('/recipe/<int:recipe_id>/rate', methods=['POST'])
def rate_recipe(recipe_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    rating = request.form.get('rating', type=int)
    if not rating or rating < 1 or rating > 5:
        flash("Please select a rating between 1 and 5.")
        return redirect(url_for('recipes.view_recipe', recipe_id=recipe_id))

    db = get_db()
    db.execute("""
        INSERT INTO ratings (user_id, recipe_id, rating) VALUES (?, ?, ?)
        ON CONFLICT(user_id, recipe_id) DO UPDATE SET rating = ?, updated_at = CURRENT_TIMESTAMP
    """, (session['user_id'], recipe_id, rating, rating))
    db.commit()
    flash("Rating submitted!")
    return redirect(url_for('recipes.view_recipe', recipe_id=recipe_id))
