from django.shortcuts import redirect
from flask import Blueprint, jsonify, request

index = Blueprint("index", __name__)

@index.route("/")
@index.route("/home")
def home():
    return jsonify({"msg": "Welcome!"})

@index.route("/user")
def user():
    return redirect()


@index.route("/identify")
def identy():
    pass