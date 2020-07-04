from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, world!"


@app.route("/adam")
def adam():
    return "Cześć, Adam!"


@app.route("/ewa")
def ewa():
    return """          Cześć
    
    ,     Ewa"""