from flask import Flask
from .routes.index import index

def create_app():
    # create an instance
    app = Flask(__name__)

    # set blueprints
    app.register_blueprint(index)


    return app