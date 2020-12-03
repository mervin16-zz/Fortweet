from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO, emit
from flask_jwt_extended import JWTManager
from flask import Flask
import app.messages.response_errors as Err
import app.models.admin as admin_mod
import app.admin as admin
import app.live as live
import app.api as api
import app.setup.database as database
import app.setup.settings as settings
import app.services.streamer as streamer


def create_app():
    # Create a Flask Application
    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static",
        instance_relative_config=True,
    )

    # Register blueprints
    app.register_blueprint(admin.admin, url_prefix="/admin")
    app.register_blueprint(live.live, url_prefix="/web")
    app.register_blueprint(api.api_bp, url_prefix="/api")

    # Flask configurations
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"sqlite:///{settings.TwitterSettings.get_instance().database_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.secret_key = settings.TwitterSettings.get_instance().jwt_secret_key

    # SQLAlchemy configurations
    database.db.app = app
    database.db.init_app(app)
    app.app_context().push()
    database.db.create_all()

    return app


# Create the app
app = create_app()

# JWT Configurations
jwt = JWTManager(app)

# Socket IO
socketio = SocketIO(app, cors_allowed_origins="*")

# Creates default admins and insert in db
for admin in settings.TwitterSettings.get_instance().super_admins:
    admin = admin_mod.AdminModel(admin["email"], admin["username"], admin["password"])
    admin.insert()

# Main error handlers
@app.errorhandler(404)  # Handling HTTP 404 NOT FOUND
def page_not_found(e):
    return Err.ERROR_NOT_FOUND


# Listen for hello emit data
# from client
@socketio.on("hello-stream")
def is_stream_active(hello_stream):
    emit("hello-reply", streamer.StreamerInit.is_stream_active(), broadcast=True)


# Start the app
if __name__ == "__main__":
    # TODO("Remove debug before deploying")
    socketio.run(app, host="0.0.0.0", debug=True)

