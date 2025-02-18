#!/usr/bin/python3
"""Starting a Flask web app.
The app listens on 0.0.0.0, port 5000.
Routes:
    - /: Displays 'Hello HBNB!'
    - /hbnb: Displays 'HBNB'
    - /c/<text>: Displays 'C' followed by the value of the text variable
    - /number/<n>: Displays 'n is a number' only if n is an integer
    - /number_template/<n>: Displays a HTML page only if n is an integer
    -/number_odd_or_even/<n>: display a HTML page only if n is an integer:
    -H1 tag: “Number: n is even|odd” inside the tag BODY
"""

from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays a message"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Displays C followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """Displays Python followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Displays a HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
