#!/usr/bin/env python3


"""Flask app"""

from flask import Flask, jsonify, request, abort, redirect
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
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
