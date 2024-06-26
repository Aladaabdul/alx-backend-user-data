#!/usr/bin/env python3


"""session_auth.py view"""


from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os
from typing import Tuple


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login() -> Tuple[str, int]:
    """routes for the Session authentication

    """
    email = request.form.get('email')
    password = request.form.get('password')

    if email is None or len(email.strip()) == 0:
        return jsonify({"error": "email missing"}), 400

    if password is None or len(password.strip()) == 0:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 401
    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    SESSION_NAME = os.getenv("SESSION_NAME", "_my_session_id")
    session_id = auth.create_session(getattr(user, 'id'))
    res = jsonify(user.to_json())
    res.set_cookie(SESSION_NAME, session_id)
    return res


@app_views.route(
        "/auth_session/logout",
        methods=["DELETE"],
        strict_slashes=False
        )
def destroy() -> Tuple[str, int]:
    """destroy route

    """
    from api.v1.app import auth
    destroy = auth.destroy_session(request)
    if not destroy:
        abort(404)
    return jsonify({})
