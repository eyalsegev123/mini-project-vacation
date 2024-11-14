# backend/app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Add your configurations (database, etc.)
    app.config['SECRET_KEY'] = 'your_secret_key'

    from .routes import main
    app.register_blueprint(main)

    return app

# hey there
