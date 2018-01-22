import os
from flask import Flask, session


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def indexPage():
    return app.send_static_file('index.html')
