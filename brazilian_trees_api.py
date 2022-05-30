from genericpath import exists
from flask import Flask
from back.modules.db import create_db
from routes.routes import Api

if( not exists( "database.db" ) ):
    create_db()

app = Flask(__name__)

app.register_blueprint(Api, url_prefix='/api')

