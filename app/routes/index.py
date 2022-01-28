from flask import Blueprint, redirect, jsonify, request, url_for, session
from config import DISCORD_LOGIN_URL
from ..utils.oauth2 import Oauth2

index = Blueprint("index", __name__)


@index.route("/")
@index.route("/home")
def home():
    return jsonify({"msg": "Welcome!"})


@index.route("/login")
def redirect_to_discord_url():
    if "user" in session:
        return redirect(url_for("index.user_data"))
    return redirect(DISCORD_LOGIN_URL)


@index.route("/identify", methods=["GET"])
def identy():
    if "user" in session:
        return redirect(url_for("index.user_data"))

    code = request.args.get("code")
    token = Oauth2.get_token(code)
    data = Oauth2.get_user(token)
    session["user"] = data
    return redirect(url_for("index.user_data"))


@index.route("/user", methods=["GET"])
def user_data():
    if "user" not in session:
        return redirect(url_for("index.home"))
    return session["user"]
