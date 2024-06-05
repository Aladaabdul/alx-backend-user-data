#!/usr/bin/env python3


"""SessionAuth class implementation"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """SessionAuth class

    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create_session function

        """
        if user_id is None:
            return None
        if type(user_id) is str:
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """user_id_for_session_id function

        """
        if session_id is None:
            return None
        if type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)
