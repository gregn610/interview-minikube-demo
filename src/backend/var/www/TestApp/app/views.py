from flask import render_template
from app import app

@app.route('/')
def home():
   return "backend!"

@app.route('/api/v1/colour.json')
def template():
    return render_template('v1/colour.json')
