from flask import Blueprint
from front.routes.trees_routes import routeTrees
from front.routes.greetings import Greetings

Render = Blueprint('front_routes', __name__,)

Render.register_blueprint(routeTrees, url_prefix='/trees')
Render.register_blueprint( Greetings, url_prefix='/')