import os
import sqlite3
from flask import Flask, g


def get_db():
    """Get a database connection for the current request."""
    if 'db' not in g:
        g.db = sqlite3.connect(
            g.database_path,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
        g.db.execute("PRAGMA foreign_keys = ON")
    return g.db


def close_db(e=None):
    """Close the database connection at the end of request."""
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db(app):
    """Create tables if they don't exist."""
    schema_path = os.path.join(os.path.dirname(__file__), '..', 'schema.sql')
    with app.app_context():
        db = sqlite3.connect(app.config['DATABASE'])
        with open(schema_path, 'r') as f:
            db.executescript(f.read())
        db.close()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    @app.before_request
    def before_request():
        g.database_path = app.config['DATABASE']

    app.teardown_appcontext(close_db)

    init_db(app)

    # Seed data on first run
    from seed_data import seed_database
    seed_database(app.config['DATABASE'])

    from app.routes.auth import auth_bp
    from app.routes.recipes import recipes_bp
    from app.routes.profile import profile_bp
    from app.routes.favorites import favorites_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(recipes_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(favorites_bp)

    return app
