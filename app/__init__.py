from flask import Flask
from datetime import timedelta
from .routes.index import index
from .utils.error import page_not_found

def create_app():
    # create an instance
    app = Flask(__name__)

    # set blueprints
    app.register_blueprint(index)

    # set error handler
    app.register_error_handler(404, page_not_found)

    return app