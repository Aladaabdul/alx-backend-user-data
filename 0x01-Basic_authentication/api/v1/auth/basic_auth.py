#!/usr/bin/env python3


"""BasicAuth class implementation"""


from api.v1.auth.auth import Auth


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
