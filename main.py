# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/templated-index')
def templated_index():
    thing_to_greet = 'World'
    return render_template('basic.html',
        thing_to_greet=thing_to_greet)


@app.route('/prettyish-index')
def prettyish_index():
    return render_template('index.html')
