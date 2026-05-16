from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash
from app import get_db

profile_bp = Blueprint('profile', __name__)


@profile_bp.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    user_id = session['user_id']
    db = get_db()
    user = db.execute("SELECT username, created_at FROM users WHERE id = ?", (user_id,)).fetchone()
    return render_template('profile.html', username=user['username'], created_at=user['created_at'])


@profile_bp.route('/update_profile', methods=['GET', 'POST'])
def update_profile():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    user_id = session['user_id']
    db = get_db()

    if request.method == 'POST':
        new_username = request.form['username']
        new_password = request.form['password']

        if new_password:
            new_password_hash = generate_password_hash(new_password)
            db.execute("UPDATE users SET username = ?, password_hash = ? WHERE id = ?",
                       (new_username, new_password_hash, user_id))
        else:
            db.execute("UPDATE users SET username = ? WHERE id = ?",
                       (new_username, user_id))

        db.commit()
        flash("Profile updated successfully!")
        return redirect(url_for('profile.profile'))

    current_username = db.execute("SELECT username FROM users WHERE id = ?", (user_id,)).fetchone()['username']
    return render_template('update_profile.html', current_username=current_username)


@profile_bp.route('/delete_profile', methods=['POST'])
def delete_profile():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    user_id = session['user_id']
    db = get_db()
    db.execute("DELETE FROM favorites WHERE user_id = ?", (user_id,))
    db.execute("DELETE FROM ratings WHERE user_id = ?", (user_id,))
    db.execute("DELETE FROM users WHERE id = ?", (user_id,))
    db.commit()
    session.clear()
    flash("Your profile has been deleted.")
    return redirect(url_for('auth.signup'))
