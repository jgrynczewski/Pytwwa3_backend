import datetime

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.datetime.now()
    if (now.month == 1 and now.day == 1):
        var="Tak"
    else:
        var="Nie"
    return render_template("index.html", context=var)


@app.route("/newyear")
def index2():
    now = datetime.datetime.now()
    var = now.month == 7 and now.day == 5
    return render_template("index2.html", context=var)


@app.route("/new")
def index3():
    now = datetime.datetime.now()
    var = now.month == 7 and now.day == 5
    return render_template("index3.html", context=var)
