#!/usr/bin/python3
'''An example of a simple web application using Flask.
'''
from flask import Flask

app = Flask(__name__)
'''Creating an instance of the Flask application.'''
app.url_map.strict_slashes = False

@app.route('/')
def index():
    '''Handler for the home route.'''
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    '''Handler for the /hbnb route.'''
    return 'HBNB'

if __name__ == '__main__':
    '''Runs the application on the specified host and port.'''
    app.run(host='0.0.0.0', port='5000')
