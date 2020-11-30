from flask_jwt_extended import JWTManager
from flask import Flask
from flask_restful import Api
from app.setup.settings import TwitterSettings
from app.setup.database import db


def create_app():
    # Create a Flask Application
    app = Flask(__name__, template_folder="../templates", static_folder="../static")

    # Flask configurations
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"sqlite:///../{TwitterSettings.get_instance().database_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.secret_key = TwitterSettings.get_instance().jwt_secret_key
    api = Api(app)

    # SQLAlchemy configurations
    db.app = app
    db.init_app(app)
    app.app_context().push()
    db.create_all()

    # JWT Configurations
    jwt = JWTManager(app)

    return app, api, jwt
