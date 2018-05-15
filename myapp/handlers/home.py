
from flask import render_template
from myapp import app


@app.route('/')
def homepage():
    handlers = [
        ('check site', '/check'),
        ('most popular', '/api/1/w3val/getstats')
    ]
    return render_template('home.html', handlers=handlers)
