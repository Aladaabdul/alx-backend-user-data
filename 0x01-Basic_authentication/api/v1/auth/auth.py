#!/usr/bin/env python3


"""API authentication module"""

from flask import request
from typing import List, TypeVar


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
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user function

        """
        return None
