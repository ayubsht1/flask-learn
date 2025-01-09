from flask import Blueprint, render_template, request, redirect, url_for
from app.models import db, Todo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@main.route('/add', methods=['POST'])
def add():
    task_text = request.form.get('task')
    new_task = Todo(text=task_text)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/complete/<int:task_id>')
def complete(task_id):
    task = Todo.query.get(task_id)
    task.complete = not task.complete
    db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/delete/<int:task_id>')
def delete(task_id):
    task = Todo.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('main.index'))
