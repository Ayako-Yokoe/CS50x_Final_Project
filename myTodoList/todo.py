from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from myTodoList.db import get_db

bp = Blueprint('todo', __name__)

# Render all tasks when GET, and create new tasks when POST
@bp.route('/', methods=('GET', 'POST'))
def index():

    if request.method == 'POST':
        day = request.form['day']
        newTask = request.form['newTask']
        duedate = request.form['duedate']
        priority = request.form['priority']
        completed = False
        error = None

        if not day:
            error = 'Date is required.'
        if not newTask:
            error = 'New task is required.'
        if not duedate:
            duedate = ''
        if not priority:
            priority = ''

        if error is not None:
            flash(error)

        else:
            db = get_db()
            db.execute(
                "INSERT INTO tasks (day, task, duedate, priority, completed) VALUES (?, ?, ?, ?, ?)", 
                ( day, newTask, duedate, priority, completed)
                )
            db.commit()
            return redirect(url_for('todo.index'))

        return render_template('todo/index.html')

    else:
        db = get_db()                                   
        tasks = db.execute(
            "SELECT id, strftime('%Y/%m/%d', day) AS day, task, strftime('%m/%d %H:%M', duedate) AS duedate, priority, completed FROM tasks"
            ).fetchall()

        return render_template('todo/index.html', tasks=tasks)

# Query tasks by id
def get_task(id):
    db = get_db()
    task = db.execute(
        "SELECT strftime('%Y-%m-%d', day) AS day, task, strftime('%m-%d %H:%M:%S', duedate) AS duedate, priority FROM tasks WHERE id=?", (id,)
        ).fetchone()

    if task is None:
        abort(404, f"Task id {id} doesn't exist.")
    
    return task

# Edit single task
@bp.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    task = get_task(id)

    if request.method == 'POST':
        newTask = request.form['newTask']
        duedate = request.form['duedate']
        priority = request.form['priority']
        error = None

        if not newTask:
            error = 'New task is required.'

        if error is not None:
            flash(error)

        else:
            db = get_db()
            db.execute(
                'UPDATE tasks SET task=?, duedate=?, priority=? WHERE id=?', 
                (newTask, duedate, priority, id,)
                )
            db.commit()
            return redirect(url_for('todo.index'))

    return render_template('todo/edit.html', task=task)


# Delete single task
@bp.route('/<int:id>/delete', methods=('GET', 'POST'))
def delete(id):
    get_task(id)
    db = get_db()
    db.execute('DELETE FROM tasks WHERE id=?', (id,))
    db.commit()
    return redirect(url_for('todo.index'))
