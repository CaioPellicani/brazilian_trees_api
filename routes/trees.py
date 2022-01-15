from crypt import methods
from datetime import datetime
from flask import Blueprint, jsonify, make_response, request
from modules.db import get_db_connection
from modules.trees_query import getTreesBy
from modules.commons import error404

routeTrees = Blueprint('trees', __name__,)

def getMaker( data ):
    result = [{"timestamp": datetime.now()}] 
    result.append( getTreesBy( data ) )
    if( len( result ) == 0 ):
        return error404( data )
    return make_response( jsonify(result) )   


@routeTrees.route('/id/<data>', methods=[ 'GET' ] )
def trees_id(data):
    if( request.method == 'GET'):
        return getMaker( { "id": data } )

@routeTrees.route('/scientific_name/<data>', methods=[ 'GET' ] )
def trees_sci_name(data):    
    if( request.method == 'GET'):
        return getMaker( { "scientific_name": data } )

@routeTrees.route('/ecological_class/<data>', methods=[ 'GET' ] )
def trees_eco_class(data):   
    if( request.method == 'GET'):
        return getMaker( { "ecological_class": data } )

@routeTrees.route('/botanical_family/<data>', methods=[ 'GET' ] )
def trees_botanical_family(data):   
    if( request.method == 'GET'):
        return getMaker( { "botanical_family": data } )

