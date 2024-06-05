#!/usr/bin/env python3


"""BasicAuth class implementation"""


from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """Basic Auth authentication

    """
    def extract_base64_authorization_header(
            self,
            authorization_header: str
            ) -> str:
        """extract_base64_authorization_header function

        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if authorization_header.startswith('Basic '):
            return authorization_header.split(' ')[1]
        else:
            return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """decode_base64_authorization_header function

        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            decode_value = base64.b64decode(base64_authorization_header)
            return decode_value.decode('utf-8')
        except (TypeError, ValueError):
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> (str, str):
        """extract_user_credentials function

        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) is not str:
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        else:
            return decoded_base64_authorization_header.split(':')

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str
            ) -> TypeVar('User'):
        """user_object_from_credentials function

        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        users = User.search({'email': user_email})
        if not users:
            return None
        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user

        """
        authorization_header = self.authorization_header(request)
        if authorization_header is None:
            return None
        extract_base64_authorization_header = self.extract_base64_authorization_header(authorization_header)
        if extract_base64_authorization_header is None:
            return None
        decode_base64_authorization_header = self.decode_base64_authorization_header(extract_base64_authorization_header)
        if decode_base64_authorization_header is None:
            return None
        user_email, user_pwd = self.extract_user_credentials(decode_base64_authorization_header)
        if user_email is None or user_pwd is None:
            return None
        return self.user_object_from_credentials(user_email, user_pwd)
