from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
bootstrap=Bootstrap()


def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    from .majority import majority as majority_blueprint
    app.register_blueprint(majority_blueprint)
    from .calculator import calculator as calculator_blueprint
    app.register_blueprint(calculator_blueprint)
    bootstrap.init_app(app)
    db.init_app(app)
    return app
