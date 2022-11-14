import os
from flask import Flask, render_template
from flask_fontawesome import FontAwesome


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'myTodoList.sqlite'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    fa = FontAwesome(app)

    from . import db
    db.init_app(app)

    from . import todo
    app.register_blueprint(todo.bp)
    app.add_url_rule('/', endpoint='index')

    from . import list
    app.register_blueprint(list.bp)
    app.add_url_rule('/list', endpoint='list')
    
    return app




# . venv/bin/activate
# flask --app myTodoList --debug run