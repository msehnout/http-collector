from flask import Flask, request
from flask import jsonify
from flask.logging import default_handler

import logging
import os


def setup_logging(flask_app):
    """Perform the setup of logging for this application."""
    if not flask_app.debug:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(
            '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))
        log_level = os.environ.get('FLASK_LOGGING_LEVEL', logging.getLevelName(logging.INFO))
        handler.setLevel(log_level)

        flask_app.logger.removeHandler(default_handler)
        flask_app.logger.addHandler(handler)
        flask_app.logger.setLevel(logging.DEBUG)


def create_app(test_config=None):
    app = Flask(__name__)

    setup_logging(app)

    @app.route("/submit", methods=['POST'])
    def submit():
        body = request.get_json()
        app.logger.info(str(body))
        return jsonify({'result': 'success'})

    return app
