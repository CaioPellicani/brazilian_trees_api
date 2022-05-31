from genericpath import exists
from flask import Flask
from back import create_db
from back import Api
from front import Render

create_db()

app = Flask(__name__, template_folder="./front/templates")

app.register_blueprint( Api, url_prefix='/api' )

app.register_blueprint( Render, url_prefix='/' )
