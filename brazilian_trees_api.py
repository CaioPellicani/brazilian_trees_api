from crypt import methods
from genericpath import exists
from flask import Flask, request, json
from routes.root_route import RootRoute
from routes.trees import routeTrees
from modules.db import create_db

if( not exists( "database.db" ) ):
    create_db()

app = Flask(__name__)

app.register_blueprint(RootRoute, url_prefix='/root')
app.register_blueprint(routeTrees, url_prefix='/trees')

@app.route('/teste', methods=[ 'GET', 'POST' ] )
def teste():
    if ( request.method == 'GET' ):
        return '{"teste":"get"}'
    elif ( request.method == "POST" ):
        data = json.loads( request.data )
        print( data['valor'] )
        return '{"teste":"post"}'
