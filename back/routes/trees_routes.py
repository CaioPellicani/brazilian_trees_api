from datetime import datetime
from flask import Blueprint, jsonify, make_response, request, json, render_template
from itsdangerous import json
from back.models.class_tree import Tree
from back.modules.trees_query import getTreesBy
from back.modules.commons import error404

routeTrees = Blueprint('trees', __name__,)

@routeTrees.route( '/', methods = [ 'GET', 'POST', 'PUT' ] )
def trees_root():
    if( request.method == 'GET' ):
        data = {}
        if( request.data ):
            data = json.loads( request.data )
        return getMaker( data )

    if( request.method == 'POST' ):
        data = json.loads( request.data )
        if( type( data ) == list ):
            result = Tree( data[0] )
        else:
            result = Tree( data )
        try:
            return jsonify( id = result.post() )
        except ValueError as x:
            return jsonify( error = f"{x.args[0]}" ) 

    if( request.method == 'PUT' ):
        data = json.loads( request.data )
        if( type( data ) == list ):
            result = Tree( data[0] )
        else:
            result = Tree( data )
        try:
            return jsonify( id = result.put() )
        except ValueError as x:
            return jsonify( error = f"{x.args[0]}" )          


def getMaker( data ):
    result = {
        "timestamp": datetime.now(), 
        "data":[]
    }
    treeList = []
    if( type( data ) == list ):
        for i in data:          
            result["data"].append( getTreesBy( i ) )
    else:
        result["data"].append( getTreesBy( data ) )
    
    if( len( result["data"] ) == 0 ):
        return error404( data )

    #result["data"].append(treeList)

    return make_response( jsonify(result) )

@routeTrees.route('/id/<data>' )
def trees_id(data): 
    return getMaker( { "id": data } ) 

@routeTrees.route('/scientific_name/<data>' )
def trees_sci_name(data): 
    return getMaker( { "scientific_name": data } )

@routeTrees.route('/popular_name/<data>' )
def trees_pop_name(data): 
    return 'TODO'

@routeTrees.route('/ecological_class/<data>' )
def trees_eco_class(data):   
    return getMaker( { "ecological_class": data } )

@routeTrees.route('/botanical_family/<data>' )
def trees_botanical_family(data):   
    return getMaker( { "botanical_family": data } )

