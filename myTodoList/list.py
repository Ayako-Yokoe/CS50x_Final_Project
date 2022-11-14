from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from myTodoList.db import get_db
from datetime import date

bp = Blueprint('list', __name__)


# Render all tasks when GET, and render selected tasks when POST
@bp.route('/list', methods=('GET', 'POST'))
def index():

    # Display tasks of the selected day, order by priority and due date
    if request.method == 'POST':
        day = request.form['day']
        error = None

        if not day:
            error = 'Date is required.'

        if error is not None:
            flash(error)

        else:
            db = get_db()
            tasks = db.execute(
                "SELECT id, strftime('%Y/%m/%d', day) AS day, task, strftime('%m/%d %H:%M', duedate) AS duedate, priority, completed FROM tasks WHERE day=? ORDER BY priority, duedate", (day,)
                ).fetchall()
            
            return render_template('list/list.html', tasks=tasks)   

    # Display all tasks, order by priority and due date
    else:
        db = get_db()                                   
        tasks = db.execute(
            "SELECT id, strftime('%Y/%m/%d', day) AS day, task, strftime('%m/%d %H:%M', duedate) AS duedate, priority, completed FROM tasks ORDER BY priority, duedate"
            ).fetchall()

        return render_template('list/list.html', tasks=tasks)


# Query task by id
def get_task(id):
    db = get_db()
    task = db.execute(
        "SELECT strftime('%Y/%m/%d', day) AS day, task, strftime('%m/%d %H:%M', duedate) AS duedate, priority FROM tasks WHERE id=?", (id,)
        ).fetchone()

    if task is None:
        abort(404, f"Task id {id} doesn't exist.")
    
    return task


# Handle completed/incompleted
@bp.route('/<int:id>/completed', methods=('GET', 'POST'))
def completed(id):
    task = get_task(id)

    if request.method == 'POST':
        completed = request.form['completed']

        db = get_db()
        status = db.execute('SELECT completed FROM tasks WHERE id=?', (id,))
        
        # Negate value
        for st in status:
            updatedComplete = 1 if st[0] == 0 else 0

        db.execute('UPDATE tasks SET completed=? WHERE id=?', (updatedComplete, id,))
        db.commit()
        return redirect(url_for('list.index'))

    return render_template('list/list.html', task=task)


# Update values for following days
@bp.route('/list/done', methods=('GET', 'POST'))
def done():
        db = get_db()

        # Move imcompleted task to the following day
        today = date.today()
        db.execute(
            "UPDATE tasks SET day=DATE(day, '+1 day') WHERE day=? AND completed = 0", (today,))
        db.commit()

        # Delete completed task from table
        db.execute('DELETE FROM tasks WHERE completed = 1')
        db.commit()

        return redirect(url_for('list.index'))
