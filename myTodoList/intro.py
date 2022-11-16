from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

bp = Blueprint('intro', __name__)

@bp.route('/intro', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        return redirect(url_for('todo.index'))
 
    else:
        return render_template('introduction/intro.html')
