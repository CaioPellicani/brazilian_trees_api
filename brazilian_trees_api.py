from genericpath import exists
from flask import Flask, json
from routes.root_route import RootRoute
from modules.db import create_db

if( not exists( "database.db" ) ):
    create_db()

app = Flask(__name__)

app.register_blueprint(RootRoute, url_prefix='/')
