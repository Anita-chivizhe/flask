from flask import Flask, render_template
from config import Config
from routes.main_bp import main_bp
from routes.movies_bp import movies_bp
from routes.movies_list_bp import movies_list_bp
from extensions import db
from sqlalchemy.sql import text

def create_app():
app = Flask(**name**)
app.config.from_object(Config)

    # Initialize the DB
    db.init_app(app)

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

    return app

if **name** == "**main**":
app = create_app()
app.run(debug=True)

# Ctrl + ~ -> Open and close terminal
