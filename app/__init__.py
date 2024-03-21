from flask import Flask
from flask_smorest import Api

from Config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

# Registering bp for both director and movies

from resources.movies import bp as movie_bp
app.register_blueprint(movie_bp)
from resources.directors import bp as director_bp
app.register_blueprint(director_bp)

