# Import flask utilities
from flask import Flask

# Import apps utilities like register config and blueprints
from .utils import register_blueprints, load_config

# Import db defaults
from myapp.extensions.db import db as db_default

# Import blueprints
# --> from myapp.blueprints.<module_name> import <bluprint_variable> as <name_blueprint>
from myapp.blueprints.home.app import home as home_blueprint
from myapp.blueprints.users.app import users as users_blueprint


def create_app(json_file='config.json', db=db_default):
    app = Flask(__name__)
    try:
        load_config(app, json_file)
    except Exception as e:
        print(e.args[0])

    # Register blueprints --> app.register_blueprint(<blueprint_name>)
    register_blueprints(app, [
        home_blueprint,
        users_blueprint,
    ])

    db.init_app(app)

    return app
