import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.urandom(24)
    DATABASE = os.path.join(BASE_DIR, 'recipe.db')
