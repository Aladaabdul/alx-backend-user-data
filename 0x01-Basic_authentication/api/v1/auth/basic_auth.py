#!/usr/bin/env python3


"""BasicAuth class implementation"""


from api.v1.auth.auth import Auth
import base64


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
