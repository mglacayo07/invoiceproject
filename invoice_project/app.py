from flask import Flask
from flask_restx import Api

def create_app():

    app = Flask(__name__)

    api = Api(app, version='0.1', title='Invoice Proyect', description='Back End Programming Exercise')

    from invoice_project.db import db, db_config
    app.config['RESTX_MASK_SWAGGER'] = False
    app.config.update(db_config)
    db.init_app(app)
    app.db = db

    return app