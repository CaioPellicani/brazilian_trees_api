from flask import Blueprint
from .trees_routes import routeTrees
from .greetings import Greetings

Render = Blueprint('front_routes', __name__,)

Render.register_blueprint(routeTrees, url_prefix='/trees')
Render.register_blueprint( Greetings, url_prefix='/')