#!/usr/bin/env python3


"""Flask app"""

from flask import Flask, jsonify, request, abort, redirect, url_for
from auth import Auth


app = Flask(__name__)

AUTH = Auth()


@app.route('/', methods=["GET"], strict_slashes=False)
def message():
    """Get message route

    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=["POST"], strict_slashes=False)
def users():
    """Post users route

    """
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


@app.route('/sessions', methods=["POST"], strict_slashes=False)
def sessions():
    """sessions

    """
    email = request.form.get("email")
    password = request.form.get("password")

    user = AUTH.valid_login(email, password)
    if user:
        session_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", session_id)
        return response
    else:
        abort(401)


@app.route('/sessions', methods=["DELETE"], strict_slashes=False)
def logout() -> str:
    """delete session

    """
    session_id = request.cookies.get("session_id")

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    Auth.destroy_session(user.id)
    return redirect(url_for("home"))


@app.route('/profile', methods=["GET"], strict_slashes=False)
def profile() -> str:
    """profile

    """
    try:
        session_id = request.cookies.get("session_id")
    except ValueError:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=["POST"], strict_slashes=False)
def get_reset_password_token() -> str:
    """get_reset_password_token

    """
    email = request.form.get("email")

    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        reset_token = None
    if reset_token is None:
        abort(403)
    return jsonify({"email": email, "reset_token": reset_token})


@app.route('/reset_password', methods=["PUT"], strict_slashes=False)
def update_password() -> str:
    """update_password

    """
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    is_password_changed = False

    try:
        Auth.update_password(reset_token, new_password)
        is_password_changed = True
    except ValueError:
        is_password_changed = False
    if not is_password_changed:
        abort(403)
    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
