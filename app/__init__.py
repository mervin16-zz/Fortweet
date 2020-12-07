from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO, emit
from flask_jwt_extended import JWTManager
from flask import Flask
import os
import app.messages.response_errors as Err
import app.models.admin as admin_mod
import app.admin as admin
import app.live as live
import app.api as api
import app.setup.settings as settings
import app.services.streamer as streamer
import app.setup.database as database


def prelims():
    # Checks if folder to database exists
    # If not, create one
    if not os.path.exists("app/databases"):
        os.makedirs("app/databases")


def create_default_admin():
    keys = settings.TwitterSettings.get_instance().super_admin
    admin = admin_mod.AdminModel(keys[0], keys[1], keys[2])
    admin.insert()


def create_app():
    # Create a Flask Application
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
        instance_relative_config=True,
    )

    my_settings = settings.TwitterSettings.get_instance()

    # Register blueprints
    app.register_blueprint(admin.admin, url_prefix="/admin")
    app.register_blueprint(live.live, url_prefix="/web")
    app.register_blueprint(api.api_bp, url_prefix="/api")

    # Flask configurations
    # app.config[
    #     "SQLALCHEMY_DATABASE_URI"
    # ] = f"postgresql+psycopg2://{my_settings.db_username}:{my_settings.db_password}@{my_settings.db_host}/{my_settings.db_name}"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///databases/fortweets.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.secret_key = my_settings.jwt_secret_key

    database.db.app = app
    database.db.init_app(app)
    database.db.create_all()

    return app


# Preliminary checks
prelims()

# Create the app
app = create_app()

# JWT Configurations
jwt = JWTManager(app)

# Socket IO
socketio = SocketIO(app, cors_allowed_origins="*")

# Creates default admins and insert in db
create_default_admin()

# Main error handlers
@app.errorhandler(404)  # Handling HTTP 404 NOT FOUND
def page_not_found(e):
    return Err.ERROR_NOT_FOUND


# Listen for hello emit data
# from client
@socketio.on("hello-stream")
def is_stream_active(hello_stream):
    emit("hello-reply", streamer.StreamerInit.is_stream_active(), broadcast=True)
