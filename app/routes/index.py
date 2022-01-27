from flask import Blueprint, redirect, jsonify, request
from config import DISCORD_LOGIN_URL
from ..utils.oauth2 import Oauth2

index = Blueprint("index", __name__)


@index.route("/")
@index.route("/home")
def home():
    return jsonify({"msg": "Welcome!"})


@index.route("/user")
def get_user_info():
    return redirect(DISCORD_LOGIN_URL)


@index.route("/identify", methods=["GET"])
def identy():
    code = request.args.get("code")
    token = Oauth2.get_token(code)
    user_data = Oauth2.get_user(token)

    return user_data
