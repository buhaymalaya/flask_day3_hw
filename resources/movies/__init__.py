from flask_smorest import Blueprint

bp = Blueprint("movies", __name__, description="Routes for Movies")

from . import routes