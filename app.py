from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'user'  # Change this to your MySQL username
app.config['MYSQL_PASSWORD'] = 'pwd'  # Change this to your MySQL password
app.config['MYSQL_DB'] = 'dbname'  # Change this to your MySQL database name

mysql = MySQL(app)

# Home Route
@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    try:
        cur.execute("SELECT id, title, rating FROM recipes ORDER BY created_at DESC LIMIT 3")  # Fetch latest 3 recipes
        recipes = cur.fetchall()
        return render_template('homepage.html', recipes=recipes)
    finally:
        cur.close()

@app.route('/find_recipe', methods=['POST'])
def find_recipe():
    if 'user_id' not in session:
        return redirect(url_for('login'))

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
    
    cur = mysql.connection.cursor()
    try:
        cur.execute("INSERT INTO search_logs (user_id, ingredients_input) VALUES (%s, %s)",
                    (user_id, ingredients_input))
        mysql.connection.commit()

        ingredient_ids = []
        categories = ['vegetable', 'dairy', 'protein', 'spice', 'grain', 'other']
        for category, items in zip(categories, [vegetables, dairy, protein, spices, grains, others]):
            for item in items:
                cur.execute("SELECT id FROM ingredients WHERE name = %s AND category = %s", (item, category))
                ingredient = cur.fetchone()
                if ingredient:
                    ingredient_ids.append(ingredient[0])

        recipe = None
        ingredients_for_template = []
        if ingredient_ids:
            placeholders = ', '.join(['%s'] * len(ingredient_ids))
            query = f"""
            SELECT r.id, r.title, r.description, r.steps, r.rating
            FROM recipes r
            JOIN recipe_ingredients ri ON r.id = ri.recipe_id
            WHERE ri.ingredient_id IN ({placeholders})
            GROUP BY r.id
            HAVING COUNT(DISTINCT ri.ingredient_id) >= 1
            LIMIT 1
            """
            cur.execute(query, tuple(ingredient_ids))
            recipe = cur.fetchone()

            if recipe:
                cur.execute("""
                    SELECT i.name, ri.quantity, i.category
                    FROM recipe_ingredients ri
                    JOIN ingredients i ON ri.ingredient_id = i.id
                    WHERE ri.recipe_id = %s
                """, (recipe[0],))
                ingredients_for_template = cur.fetchall()
                return render_template('view_recipe.html', recipe=recipe, ingredients=ingredients_for_template)
    finally:
        cur.close()

    flash("No recipe found with the selected ingredients. Try a different combination!")
    return redirect(url_for('recipes'))


# Signup Route
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, password))
            mysql.connection.commit()
            flash("Account created successfully. Please login.")
            return redirect(url_for('login'))
        except Exception as e:
            flash(f"An error occurred: {e}")
        finally:
            cur.close()
    return render_template('signup.html')

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        try:
            cur.execute("SELECT id, username, password_hash FROM users WHERE username = %s", (username,))
            user = cur.fetchone()

            if user and check_password_hash(user[2], password):
                session['user_id'] = user[0]
                session['username'] = user[1]
                print(f"User {user[1]} (ID: {user[0]}) logged in.") # Debug print
                return redirect(url_for('home'))
            else:
                flash("Invalid username or password")
        finally:
            cur.close()
    return render_template('login.html')

# Logout Route
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('login'))

# Profile Route
@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    cur = mysql.connection.cursor()
    try:
        cur.execute("SELECT username, created_at FROM users WHERE id = %s", (user_id,))
        user = cur.fetchone()
        return render_template('profile.html', username=user[0], created_at=user[1])
    finally:
        cur.close()

#delete profile
@app.route('/delete_profile')
def delete_profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    cur = mysql.connection.cursor()
    try:
        cur.execute("DELETE FROM favorites WHERE user_id = %s", (user_id,))
        cur.execute("DELETE FROM users WHERE id = %s", (user_id,)) # Consider cascading or nullifying recipes created by this user
        mysql.connection.commit()
        session.clear()
        flash("Your profile has been deleted.")
        return redirect(url_for('signup'))
    finally:
        cur.close()

# Update Profile Route
@app.route('/update_profile', methods=['GET', 'POST'])
def update_profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    cur = mysql.connection.cursor()
    try:
        if request.method == 'POST':
            new_username = request.form['username']
            new_password = request.form['password']

            if new_password:
                new_password_hash = generate_password_hash(new_password)
                cur.execute("UPDATE users SET username = %s, password_hash = %s WHERE id = %s",
                            (new_username, new_password_hash, user_id))
            else:
                cur.execute("UPDATE users SET username = %s WHERE id = %s",
                            (new_username, user_id))

            mysql.connection.commit()
            flash("Profile updated successfully!")
            return redirect(url_for('profile'))

        cur.execute("SELECT username FROM users WHERE id = %s", (user_id,))
        current_username = cur.fetchone()[0]
        return render_template('update_profile.html', current_username=current_username)
    finally:
        cur.close()

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    try:
        cur.execute("SELECT id, name, category FROM ingredients")
        ingredients_from_db = cur.fetchall()

        categorized_ingredients = {'vegetable': [], 'dairy': [], 'protein': [], 'spice': [], 'grain': [], 'other': []}
        for ing in ingredients_from_db:
            cat = ing[2] if ing[2] in categorized_ingredients else 'other'
            categorized_ingredients[cat].append({'id': ing[0], 'name': ing[1]})

        if request.method == 'POST':
            title = request.form['name']
            description = request.form.get('description', 'No description provided.')
            instructions = request.form['instructions']
            rating = request.form.get('rating', 0)
            user_id = session['user_id']

            cur.execute("INSERT INTO recipes (title, description, steps, created_by, rating) VALUES (%s, %s, %s, %s, %s)",
                        (title, description, instructions, user_id, rating))
            recipe_id = cur.lastrowid

            categories_map = {
                'vegetables': 'vegetable', 'dairy': 'dairy', 'proteins': 'protein',
                'spices': 'spice', 'grains': 'grain', 'others': 'other'
            }
            
            for category_form_name, category_db_name in categories_map.items():
                selected_ingredients_ids = request.form.getlist(category_form_name)
                
                for ing_id in selected_ingredients_ids:
                    quantity_key = f'quantity_{ing_id}'
                    quantity = request.form.get(quantity_key, '')
                    
                    cur.execute("INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity) VALUES (%s, %s, %s)",
                                (recipe_id, int(ing_id), quantity))
                
                new_ingredient_name = request.form.get(f'new_{category_db_name}')
                new_ingredient_quantity = request.form.get(f'new_quantity_{category_db_name}', '')

                if new_ingredient_name and new_ingredient_name.strip():
                    cur.execute("SELECT id FROM ingredients WHERE name = %s AND category = %s", (new_ingredient_name.strip(), category_db_name))
                    existing_ingredient = cur.fetchone()
                    if not existing_ingredient:
                        cur.execute("INSERT INTO ingredients (name, category) VALUES (%s, %s)", (new_ingredient_name.strip(), category_db_name))
                        new_ingredient_id = cur.lastrowid
                    else:
                        new_ingredient_id = existing_ingredient[0]
                    
                    cur.execute("INSERT INTO recipe_ingredients (recipe_id, ingredient_id, quantity) VALUES (%s, %s, %s)",
                                (recipe_id, new_ingredient_id, new_ingredient_quantity))

            mysql.connection.commit()
            flash("Recipe submitted successfully!")
            return redirect(url_for('submit'))
    finally:
        cur.close()

    return render_template('submit.html', ingredients=categorized_ingredients)


# Recipes Route
@app.route('/recipes')
def recipes():
    cur = mysql.connection.cursor()
    try:
        cur.execute("SELECT id, title, rating FROM recipes ORDER BY created_at DESC")
        recipes = cur.fetchall()
        return render_template('recipes.html', recipes=recipes)
    finally:
        cur.close()

@app.route('/recipe2/<int:recipe_id>')
def view_recipe2(recipe_id):
    cur = mysql.connection.cursor()
    try:
        cur.execute("SELECT title, description, steps, rating FROM recipes WHERE id = %s", (recipe_id,))
        recipe = cur.fetchone()

        cur.execute("""
            SELECT i.name, ri.quantity, i.category
            FROM recipe_ingredients ri
            JOIN ingredients i ON ri.ingredient_id = i.id
            WHERE ri.recipe_id = %s
        """, (recipe_id,))
        ingredients = cur.fetchall()

        return render_template('view_recipe2.html', recipe=recipe, ingredients=ingredients)
    finally:
        cur.close()


# View Single Recipe Route
@app.route('/recipe/<int:recipe_id>')
def view_recipe(recipe_id):
    cur = mysql.connection.cursor()
    try:
        cur.execute("SELECT title, description, steps, rating FROM recipes WHERE id = %s", (recipe_id,))
        recipe = cur.fetchone()

        cur.execute("""
            SELECT i.name, ri.quantity, i.category
            FROM recipe_ingredients ri
            JOIN ingredients i ON ri.ingredient_id = i.id
            WHERE ri.recipe_id = %s
        """, (recipe_id,))
        ingredients = cur.fetchall()

        return render_template('view_recipe.html', recipe=recipe, ingredients=ingredients)
    finally:
        cur.close()


@app.route('/favorites')
def favorites():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    cur = mysql.connection.cursor()
    try:
        # Debugging: Print the user ID whose favorites are being fetched
        print(f"Fetching favorites for user_id: {user_id}")

        cur.execute("""
            SELECT r.id, r.title, r.rating
            FROM recipes r
            JOIN favorites f ON r.id = f.recipe_id
            WHERE f.user_id = %s
        """, (user_id,)) # Use the user_id variable directly here
        recipes = cur.fetchall()

        # Debugging: Print the raw query results
        print(f"Favorites query results: {recipes}")

        if not recipes:
            print("No favorite recipes found for this user.") # Debug print
            return render_template('favorites.html', recipes=None)

        return render_template('favorites.html', recipes=recipes)
    except Exception as e:
        print(f"Error fetching favorites: {e}") # Debug print
        flash("An error occurred while fetching your favorites.")
        return redirect(url_for('home')) # Redirect to home or an error page
    finally:
        cur.close()


# Add Recipe to Favorites
@app.route('/favorite/<int:recipe_id>', methods=['POST'])
def favorite(recipe_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    try:
        user_id = session['user_id']
        # Check if already favorited
        cur.execute("SELECT id FROM favorites WHERE user_id = %s AND recipe_id = %s", (user_id, recipe_id))
        existing_favorite = cur.fetchone()
        if existing_favorite:
            flash("Recipe is already in your favorites!")
        else:
            cur.execute("INSERT INTO favorites (user_id, recipe_id) VALUES (%s, %s)", (user_id, recipe_id))
            mysql.connection.commit()
            flash("Recipe added to favorites!")
    except Exception as e:
        flash(f"Error adding to favorites: {e}")
    finally:
        cur.close()
    return redirect(url_for('recipes'))

@app.route('/search_recipes', methods=['GET'])
def search_recipes():
    ingredients_param = request.args.get('ingredients', '')
    ingredient_names = [name.strip() for name in ingredients_param.split(',') if name.strip()]
    
    if not ingredient_names:
        return jsonify({'recipes': []})

    placeholders = ','.join(['%s'] * len(ingredient_names))
    query = f"""
        SELECT r.id, r.title, r.rating
        FROM recipes r
        JOIN recipe_ingredients ri ON r.id = ri.recipe_id
        JOIN ingredients i ON ri.ingredient_id = i.id
        WHERE i.name IN ({placeholders})
        GROUP BY r.id
        HAVING COUNT(DISTINCT i.name) >= %s;
    """
    
    cur = mysql.connection.cursor()
    try:
        cur.execute(query, tuple(ingredient_names + [1]))
        results = cur.fetchall()

        recipes_list = [{'id': row[0], 'title': row[1], 'rating': row[2]} for row in results]
        return jsonify({'recipes': recipes_list})
    finally:
        cur.close()


# Search Log Route
@app.route('/log_search', methods=['POST'])
def log_search():
    user_id = session.get('user_id')
    ingredients_input = request.form['ingredients_input']
    cur = mysql.connection.cursor()
    try:
        cur.execute("INSERT INTO search_logs (user_id, ingredients_input) VALUES (%s, %s)", (user_id, ingredients_input))
        mysql.connection.commit()
        return '', 204
    finally:
        cur.close()

if __name__ == '__main__':
    app.run(debug=True)