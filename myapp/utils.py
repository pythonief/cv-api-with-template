import json
from flask import Flask
from flask.logging import create_logger


def load_config(app: Flask, json_file):
    if isinstance(json_file, str):
        app.config.from_file(json_file, load=json.load)
        app.config['MODE'] = "prod"
    try:
        with open('myapp/secret.json') as f:
            app.config.update(json.load(f))
    except Exception as e:
        print(e)

    development_mod = app.config.get('MODE')
    if development_mod == 'dev':
        app.config['DEBUG'] = True
    elif development_mod == 'prod':
        app.config['DEBUG'] = False
    else:
        error = f'Improperly configured: MODE in "secret.json" file can be set only with "dev" or "prod" values and was set to "{development_mod}"'
        raise Exception(error)


def register_blueprints(app: Flask, blueprints: list):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def log_routes(app: Flask):

    log = create_logger(app)

    with app.app_context():
        log.info('MAP ROUTER')
        for rule in app.url_map.iter_rules():
            log.debug(f'Endpoint: {rule} methods={rule.methods}')
