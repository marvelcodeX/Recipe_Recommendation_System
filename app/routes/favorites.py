from flask import Blueprint, render_template, redirect, url_for, session, flash, request
from app import get_db

favorites_bp = Blueprint('favorites', __name__)


@favorites_bp.route('/favorites')
def favorites():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    user_id = session['user_id']
    db = get_db()
    try:
        recipes = db.execute("""
            SELECT r.id, r.title, r.description,
                   COALESCE(AVG(rt.rating), r.rating) AS avg_rating
            FROM recipes r
            JOIN favorites f ON r.id = f.recipe_id
            LEFT JOIN ratings rt ON r.id = rt.recipe_id
            WHERE f.user_id = ?
            GROUP BY r.id
        """, (user_id,)).fetchall()

        return render_template('favorites.html', recipes=recipes if recipes else None)
    except Exception:
        flash("An error occurred while fetching your favorites.")
        return redirect(url_for('recipes.home'))


@favorites_bp.route('/favorite/<int:recipe_id>', methods=['POST'])
def favorite(recipe_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    db = get_db()
    user_id = session['user_id']
    try:
        db.execute("INSERT INTO favorites (user_id, recipe_id) VALUES (?, ?)", (user_id, recipe_id))
        db.commit()
        flash("Recipe added to favorites!")
    except Exception:
        flash("Recipe is already in your favorites!")
    return redirect(url_for('recipes.view_recipe', recipe_id=recipe_id))


@favorites_bp.route('/unfavorite/<int:recipe_id>', methods=['POST'])
def unfavorite(recipe_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    db = get_db()
    db.execute("DELETE FROM favorites WHERE user_id = ? AND recipe_id = ?",
               (session['user_id'], recipe_id))
    db.commit()
    flash("Recipe removed from favorites.")

    referrer = request.referrer or url_for('favorites.favorites')
    return redirect(referrer)
