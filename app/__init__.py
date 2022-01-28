from flask import Flask
from datetime import timedelta
from .routes.index import index
from .utils.error import page_not_found
from config import SECRET_KEY

def create_app():
    # create an instance
    app = Flask(__name__)

    # set blueprints
    app.register_blueprint(index)

    # set secret key
    app.secret_key = SECRET_KEY

    # set session time
    app.permanent_session_lifetime = timedelta(minutes=5)

    # set error handler
    app.register_error_handler(404, page_not_found)

    return app