#!/usr/bin/env python3
"""Module for auth functions"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
        Hashes a password
        Args:
            (password): the password to be hashed
        Return
            the hashed password in byte format
        """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)
