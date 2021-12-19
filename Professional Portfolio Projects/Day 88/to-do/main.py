from flask import Flask, render_template, redirect, url_for, request
from datetime import date
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# TABLE Configuration
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250), nullable=False)
    completed = db.Column(db.Boolean)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


def add_task(description, completed=0):
    task = Task(
        description=description,
        completed=completed
    )
    db.session.add(task)
    db.session.commit()


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/new", methods=['GET', 'POST'])
def new_list():
    if request.method == "POST":
        add_task(request.form.get("task[description]"))
        return redirect(url_for("todo_list"))
    else:
        task_ids = [task.to_dict()['id'] for task in Task.query.all()]
        for task_id in task_ids:
            delete_task(task_id)
    return render_template("new_list.html")


@app.route("/delete-task/<int:task_id>")
def delete_task(task_id):
    db.session.delete(Task.query.get(task_id))
    db.session.commit()
    return redirect(url_for("todo_list"))


@app.route("/todo-list", methods=['GET', 'POST'])
def todo_list():
    tasks = [task.to_dict() for task in Task.query.all()]
    if request.method == "POST":
        add_task(request.form.get("task[description]"))
        return redirect(url_for("todo_list"))
    return render_template("todo_list.html", today=date.today(), tasks=tasks)


if __name__ == '__main__':
    app.run(debug=True)
