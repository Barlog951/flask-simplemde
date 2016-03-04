#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask.ext.simplemde import SimpleMDE

app = Flask(__name__)

# Using IIFE style javascript code, this is the default value
app.config['SIMPLEMDE_JS_IIFE'] = True

# Using external CDN links, this is the default value
app.config['SIMPLEMDE_USE_CDN'] = True

SimpleMDE(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
