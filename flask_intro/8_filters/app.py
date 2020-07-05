from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    a_list = [1,2,3,4,5]
    return render_template("index.html", a_list=a_list)