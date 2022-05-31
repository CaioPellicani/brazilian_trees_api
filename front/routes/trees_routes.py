from datetime import datetime
from flask import Blueprint, jsonify, make_response, request, json, render_template


routeTrees = Blueprint('trees', __name__,)

@routeTrees.route( '/', methods = [ 'GET', 'POST', 'PUT' ] )
def trees_root():
    return make_response( jsonify(  {"todo":True}))          


@routeTrees.route('/id/<data>' )
def trees_id(data): 
    return make_response( jsonify(  {"todo":True})) 

@routeTrees.route('/scientific_name/<data>' )
def trees_sci_name(data): 
    return make_response( jsonify(  {"todo":True})) 

@routeTrees.route('/popular_name/<data>' )
def trees_pop_name(data): 
    return make_response( jsonify(  {"todo":True})) 

@routeTrees.route('/ecological_class/<data>' )
def trees_eco_class(data):   
    return make_response( jsonify(  {"todo":True})) 

@routeTrees.route('/botanical_family/<data>' )
def trees_botanical_family(data):   
    return make_response( jsonify(  {"todo":True})) 

