"""
TEMPLATE PROJECT CREATED BY FRITZLER ILAN EMANUEL
JR PYTHON DEVELOPER

github: @fritzlerilan
secondary-github: @pythonief
linkedin: https://www.linkedin.com/in/ilan-fritzler
"""

from myapp.app import create_app
from myapp.utils import log_routes

# Import extensions
from myapp.extensions.db import db

# Import config file

app = create_app('config.json', db)

try:
    with app.app_context():
        db.create_all()
except Exception as e:
    print('Error in database initialization: ', e.args[0])

# Just for testing registration routes
log_routes(app)

# Inside the secret.json file, the key-value 'MODE' can be set on 'dev' or 'prod'.
# default: MODE: 'prod' if MODE is not set with a DEBUG = False behaviour
# this can be switched for debug behaviour in both enviroments -production- and -development-
if __name__ == '__main__':
    app.run()
