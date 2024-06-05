#!/usr/bin/env python3


"""API authentication module"""

from flask import request
from typing import List, TypeVar
import os


class Auth:
    """Auth class

    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth function

        """
        if path is None:
            return True
        if len(excluded_paths) == 0 or excluded_paths is None:
            return True
        if path in excluded_paths:
            return False

        n_path = path if path.endswith('/') else path + '/'

        n_excluded_paths = [
                p if p.endswith('/') else p + '/' for p in excluded_paths]
        if n_path in n_excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """authorization_header function

        """
        if request is None:
            return None
        auth = request.headers.get('Authorization')
        if auth is None:
            return None
        return auth

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user function

        """
        return None

    def session_cookie(self, request=None):
        """session_cookie function

        """
        SESSION_NAME = os.getenv('SESSION_NAME')
        if request is None:
            return None
        return request.cookies.get(SESSION_NAME)
