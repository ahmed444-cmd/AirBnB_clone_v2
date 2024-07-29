#!/usr/bin/python3
'''A straightforward web app built with Flask.
'''
from flask import Flask


app = Flask(__name__)
'''The instance of Flask app.'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''Home.'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''The hbnb page.'''
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
