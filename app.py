from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='barax', description='REST API for our guild management application.')

@app.route('/')
def hello_world():
    return 'Hello World!'
