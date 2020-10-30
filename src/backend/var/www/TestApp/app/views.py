from flask import render_template, Response
from app import app

@app.route('/')
def home():
   return "backend!"

@app.route('/api/v1/colour.json')
def template():
    ret = render_template('v1/colour.json')
    resp = Response(response=ret,
                    status=200,
                    mimetype="application/json")

    return resp