from genericpath import exists
from flask import Flask
from back.modules.db import create_db
from back.routes.routes import Api
from front.routes.routes import Render

create_db()

app = Flask(__name__, template_folder="./front/templates")

app.register_blueprint( Api, url_prefix='/api' )

app.register_blueprint( Render, url_prefix='/' )
