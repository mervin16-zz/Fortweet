from app import socketio, app

# Start the app
if __name__ == "__main__":
    from os import environ

    socketio.run(app, host="0.0.0.0", port=environ.get("PORT", 5000))
