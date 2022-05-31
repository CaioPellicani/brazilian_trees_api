from flask import Blueprint, jsonify, make_response

Greetings = Blueprint('greetings', __name__,)

@Greetings.route('/')
def greetings():
    return make_response( jsonify(  {"todo":True})) 