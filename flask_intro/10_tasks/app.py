import os

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

if os.path.isfile("tasks.txt"):
    with open("tasks.txt", 'r') as a_file:
        tasks = a_file.readlines()
else:
    with open("tasks.txt", 'w+') as a_file:
        tasks = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        with open("tasks.txt", "a") as a_file:
            a_file.write(f"{task}\n")

        tasks.append(task)
    return render_template('index.html', tasks=tasks)