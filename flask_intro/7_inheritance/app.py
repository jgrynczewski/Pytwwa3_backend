from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/first")
def first():
    return render_template("first.html")


@app.route("/second")
def second():
    return render_template("second.html")