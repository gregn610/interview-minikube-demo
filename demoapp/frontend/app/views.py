from flask import render_template
from app import app
from os import getenv

@app.route('/')
def home():
    ctx = {"BACKEND_API_PROTOCOL": getenv('BACKEND_API_PROTOCOL', 'http'),
           "BACKEND_SERVICE_HOST": getenv('BACKEND_SERVICE_HOST', 'localhost'),
           "BACKEND_SERVICE_PORT": getenv('BACKEND_SERVICE_PORT', '58081'),
           "BACKEND_API_PATH_COLOUR": getenv('BACKEND_API_PATH_COLOUR', 'api/v1/colour.json'),
           }
    return render_template('index.html', **ctx)
