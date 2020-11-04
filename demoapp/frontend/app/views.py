from flask import render_template
from app import app
from os import getenv
from urllib import request

import logging

@app.route('/')
def home():
    url = "{}://{}:{}/{}".format(
        getenv('BACKEND_API_PROTOCOL', 'http'),
        getenv('BACKEND_SERVICE_HOST', 'localhost'),
        getenv('BACKEND_SERVICE_PORT', '58081'),
        getenv('BACKEND_API_PATH_COLOUR', 'api/v1/colour.json'),
    )
    logging.warning("API URL: %s", url)
    # ToDo:
    data = request.urlopen(url).read().decode('utf-8', 'replace')
    ctx = {"JSON_DATA": data}
    return render_template('index.html', **ctx)
