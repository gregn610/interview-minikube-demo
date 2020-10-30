from flask import render_template, Response, request, make_response
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


### CORS section
# Thanks: https://stackoverflow.com/a/63400010/266387
@app.after_request
def after_request_func(response):
    origin = request.headers.get('Origin')
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Headers', 'x-csrf-token')
        response.headers.add('Access-Control-Allow-Methods',
                            'GET, POST, OPTIONS, PUT, PATCH, DELETE')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)
    else:
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)

    return response
### end CORS section