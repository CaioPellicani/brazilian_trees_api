from crypt import methods
from datetime import datetime
from flask import Blueprint, jsonify, make_response, request, json
from itsdangerous import json
from modules.db import get_db_connection
from modules.trees_query import getTreesBy
from modules.commons import error404

routeTrees = Blueprint('trees', __name__,)

def getMaker( data ):
    result = [{"timestamp": datetime.now()}]
    treeList = getTreesBy( data )
    
    if( len( treeList ) == 0 ):
        return error404( data )

    result.append(treeList)
    return make_response( jsonify(result) )

@routeTrees.route( '/', methods = [ 'GET', 'POST' ] )
def trees_root():
    if( request.method == 'GET' ):
        return getMaker( json.loads( request.data ) )

    if( request.method == 'POST' ):
        result = '{"route":"trees_root", "met":"POST" }'

    return result


@routeTrees.route('/id/<data>' )
def trees_id(data): 
    return getMaker( { "id": data } )

@routeTrees.route('/scientific_name/<data>' )
def trees_sci_name(data): 
    return getMaker( { "scientific_name": data } )

@routeTrees.route('/ecological_class/<data>' )
def trees_eco_class(data):   
    return getMaker( { "ecological_class": data } )

@routeTrees.route('/botanical_family/<data>' )
def trees_botanical_family(data):   
    return getMaker( { "botanical_family": data } )

