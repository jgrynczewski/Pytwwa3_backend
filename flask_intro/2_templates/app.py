#Szablony
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "<html><head></head><body><p>Hello, world!</p></body></html>"

@app.route("/hello")
def hello2():
    return render_template("index.html")