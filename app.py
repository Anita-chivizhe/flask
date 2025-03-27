from pprint import pprint

from flask import Flask, render_template, request

from routes.main_bp import main_bp
from routes.movie_list_bp import movies_list_bp
from routes.movies_bp import movies_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_bp)
    app.register_blueprint(movies_bp, url_prefix="/movies")
    app.register_blueprint(movies_list_bp, url_prefix="/movie-list")
    return app


if __name__ == "__main__":
    app = create_app
    app.run(debug=True)
