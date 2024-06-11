#!/usr/bin/env python3


"""Auth

"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """_hash_password

    """
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed
