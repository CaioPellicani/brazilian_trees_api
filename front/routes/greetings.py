from flask import Blueprint, render_template, make_response, jsonify
from front.commons import apiURL

import requests

Greetings = Blueprint('greetings', __name__,)

@Greetings.route('/')
def greetings():
    return render_template(
        "menu.html", 
        data=( requests.get( apiURL ).json() ) 
    )
        