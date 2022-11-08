from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from myTodoList.db import get_db

bp = Blueprint('todo', __name__)


@bp.route('/', methods=('GET', 'POST'))
def index():
    db = get_db()

    if request.method == 'POST':
        day = request.form['day']
        newTask = request.form['newTask']
        datetime = request.form['datetime']
        priority = request.form['priority']
        completed = False
        error = None

        if not day:
            error = 'Date is required.'
        if not newTask:
            error = 'New task is required.'
        if not datetime:
            datetime = ''
        if not priority:
            priority = ''

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute('INSERT INTO tasks (day, task, datetime, priority, completed) VALUES (?, ?, ?, ?, ?)', (day, newTask, datetime, priority, completed))
            db.commit()
            return redirect(url_for('todo.index'))

        return render_template('todo/index.html')   

    else:
        # tasks = db.execute('SELECT day, task, datetime, priority, completed FROM tasks')
        tasks = db.execute('SELECT * FROM tasks')

        console.log("tasks", tasks)

        return render_template('todo/index.html', tasks=tasks)

