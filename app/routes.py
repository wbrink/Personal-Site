from flask import render_template, url_for
from app import app
import os

@app.route('/')
def index():
    msg = 'Hello my name is Will'
    #img = os.path.join('static', 'Dilbert.png')
    return render_template('index.html')
