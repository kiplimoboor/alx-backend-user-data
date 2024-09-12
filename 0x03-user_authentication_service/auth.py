#!/usr/bin/env python3
"""Module for auth functions"""

import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


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


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registsers user to the database
        Args:
            (email): user email address
            (password): user password
        Return:
            the registered user
        """

        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, str(hashed_password))
            return new_user
        else:
            raise ValueError(f'User {email} already exists')
