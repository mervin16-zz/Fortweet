import threading as Corou
from flask import Flask, render_template
from service import twitterService

app = Flask(__name__)

@app.route("/")
def index():

    stream = Corou.Thread(target=twitterService.twitter_instantiation)
    stream.start()

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)