from flask import Flask
from flask_restx import Api

def create_app():
    app = Flask(__name__)

    api = Api(app, version='0.1', title='Invoice Proyect', description='Back End Programming Exercise')

    return app