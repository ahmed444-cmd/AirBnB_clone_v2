#!/usr/bin/python3
'''A basic Flask web app.
'''
from flask import Flask


app = Flask(__name__)
'''instance of Flask app.'''
app.url_map.strict_slashes = False


@app.route('/')
def index():
    '''Home'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''The hbnb pge.'''
    return 'HBNB'


@app.route('/c/<text>')
def c_page(text):
    '''The c page.'''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>')
@app.route('/python', defaults={'text': 'is cool'})
def python_page(text):
    '''The pyth page.'''
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number_page(n):
    '''The number page.'''
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
