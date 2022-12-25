from flask import Blueprint

auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return "Login"

@auth.route("/sign-up")
def sign_up():
    return "Sign up"

@auth.route("/Log-out")
def log_out():
    return "Log out"