from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/hello", methods=["POST"])
def hello():
    if request.method == "POST":
        name = request.form.get("moje_imie")
    return render_template("hello.html", name=name)
