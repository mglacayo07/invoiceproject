from flask_sqlalchemy import SQLAlchemy

db_config = {
    'SQLALCHEMY_DATABASE_URI': 'mysql+mysqlconnector://USER:PASSWORD@127.0.0.1/invoice',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
}

db = SQLAlchemy()