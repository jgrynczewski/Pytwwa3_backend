from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tasks.append(request.form.get("task"))

    return render_template('index.html', tasks=tasks)