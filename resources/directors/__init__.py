from flask_smorest import Blueprint

bp = Blueprint('directors', __name__, description= "Routes for Directors")

from . import routes