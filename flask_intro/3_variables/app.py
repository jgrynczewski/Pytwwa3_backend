import random

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    var  = "Hello"
    return render_template('index.html', context=var)


@app.route("/goodbye")
def goodbye():
    var  = "Goodbye"
    return render_template('index.html', context=var)


@app.route("/choice")
def choice():
    text = ["Hello", "Goodbye", "Good morning", "Good evening"]
    var = random.choice(text)
    return render_template("index.html", context=var)