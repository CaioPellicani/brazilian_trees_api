from flask import Blueprint
from routes.root_route import RootRoute
from routes.trees_routes import routeTrees
from routes.greetings import Greetings

Api = Blueprint('routes', __name__,)

Api.register_blueprint(RootRoute, url_prefix='/root')
Api.register_blueprint(routeTrees, url_prefix='/trees')
Api.register_blueprint( Greetings, url_prefix='/')