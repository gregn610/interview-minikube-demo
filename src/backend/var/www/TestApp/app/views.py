from flask import render_template, Response
from app import app

from os import getenv

@app.route('/')
def home():
   return "backend!"

@app.route('/api/v1/colour.json')
def template():
    # os.getenv with defaults
    ctx = {
        "demo_background_colour": getenv('DEMO_BACKGROUND_COLOUR', 'white'),
        "demo_foreground_colour": getenv('DEMO_FOREGROUND_COLOUR', 'red')
    }
    ret = render_template('v1/colour.json', **ctx)
    response = Response(response=ret,
                    status=200,
                    mimetype="application/json")

    # response.headers['X-Parachutes'] = 'parachutes are cool'

    return response
