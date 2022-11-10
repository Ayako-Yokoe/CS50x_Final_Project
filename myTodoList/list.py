from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from myTodoList.db import get_db

bp = Blueprint('list', __name__)

@bp.route('/list', methods=('GET', 'POST'))
def index():

    if request.method == 'POST':
        print("here")
        day = request.form['day']
        error = None

        print("post day", day)

        if not day:
            error = 'Date is required.'

        if error is not None:
            flash(error)

        else:
            db = get_db()
            tasks = db.execute("SELECT id, strftime('%Y-%m-%d', day) AS day, task, strftime('%m-%d %H:%M:%S', duedate) AS duedate, priority, completed FROM tasks WHERE day=?", (day)).fetchall()
            
            for task in tasks:
                print("task for", task[1])

            return render_template('list/list.html', tasks=tasks)   


    else:
        db = get_db()                                   
        tasks = db.execute("SELECT id, strftime('%Y-%m-%d', day) AS day, task, strftime('%m-%d %H:%M:%S', duedate) AS duedate, priority, completed FROM tasks").fetchall()

        return render_template('list/list.html', tasks=tasks)


def get_task(id):
    db = get_db()
    task = db.execute("SELECT strftime('%Y-%m-%d', day) AS day, task, strftime('%m-%d %H:%M:%S', duedate) AS duedate, priority FROM tasks WHERE id=?", (id,)).fetchone()

    if task is None:
        abort(404, f"Task id {id} doesn't exist.")
    
    return task


@bp.route('/<int:id>/completed', methods=('GET', 'POST'))
def completed(id):
    task = get_task(id)

    if request.method == 'POST':
        completed = request.form['completed']

        db = get_db()
        status = db.execute('SELECT completed FROM tasks WHERE id=?', (id,))
        
        for st in status:
            updatedComplete = 1 if st[0] == 0 else 0

        db.execute('UPDATE tasks SET completed=? WHERE id=?', (updatedComplete, id,))
        db.commit()
        return redirect(url_for('list.index'))

    return render_template('list/list.html', task=task)
