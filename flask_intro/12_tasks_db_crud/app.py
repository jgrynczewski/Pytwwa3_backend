import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

from models import Task

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        task = request.form.get("task")

        t = Task(text=task)
        db.session.add(t) # insert C from CRUD
        db.session.commit()


    tasks = Task.query.all() #select R from CRUD
    return render_template('index.html', tasks=tasks)


@app.route("/update/<int:task_id>", methods=['GET', 'POST'])
def update(task_id):
    task = Task.query.get(task_id)

    if request.method == "POST":
        task.text = request.form['task']

        try:
            db.session.merge(task) # update U from CRUD
            db.session.commit()
        except Exception as e:
            return "Coś poszło nie tak"

        return redirect("/")

    return render_template('update.html', task=task)


@app.route('/delete', methods=["POST"])
def delete():
    task_id = request.form.get("task_id")

    # task = Task.query.get(task_id)
    task = db.session.query(Task).get(task_id)

    db.session.delete(task)  # delete D from CRUD
    db.session.commit()

    return redirect("/")
