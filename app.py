from flask import Flask, render_template
from flask_login import LoginManager
from sqlalchemy.sql import text

from config import Config
from extensions import db
from models.movie import Movie
from models.user import Users
from routes.auth_bp import auth_bp
from routes.main_bp import main_bp
from routes.movie_list_bp import movies_list_bp
from routes.movies_bp import movies_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize the DB
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth_bp.login_page"

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(user_id)

    with app.app_context():
        try:
            result = db.session.execute(text("SELECT 1")).fetchall()
            print("Connection successful:", result)
        except Exception as e:
            print("Error connecting to the database:", e)

    # Flask - Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(movies_bp, url_prefix="/movies")  # Refactor - Mailability ⬆️
    app.register_blueprint(movies_list_bp, url_prefix="/movie-list")
    app.register_blueprint(auth_bp, url_prefix="/signup")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

# Ctrl + ~ -> Open and close terminal
