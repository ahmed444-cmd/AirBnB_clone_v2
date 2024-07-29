#!/usr/bin/python3
'''A basic web application built with Flask.
'''
from flask import Flask


app = Flask(__name__)
'''The instance of the Flask application.'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''home'''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
