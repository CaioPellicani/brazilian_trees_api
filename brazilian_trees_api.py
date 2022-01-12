from flask import Flask, json
from routes.root_route import RootRoute

app = Flask(__name__)

app.register_blueprint(RootRoute, url_prefix='/')
