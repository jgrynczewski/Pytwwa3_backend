from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def index():
    return f"Hello, world!"


@app.route("/adam")
def adam():
    return "Cześć, Adam!"


@app.route("/ewa")
def ewa():
    return """          Cześć
    
    ,     Ewa"""


# Zmienne reguły
@app.route("/witaj/<name>")
def hello(name):
    name = name.title()
    return f"Cześć, {name}"


# Konwertery. Dostępne konwertery: string, int, float, path, uuid
@app.route("/<string:name>")
def hello2(name):
    name = escape(name)
    return f"Hi, {name}"
