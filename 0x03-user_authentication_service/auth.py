#!/usr/bin/env python3
"""Module for auth functions"""

import uuid
from typing import Union

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


def _generate_uuid() -> str:
    """Generates and returns a string representation of a uuid"""
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """
        Checks if user details are valid before logging in
        Args:
            (email): email address
            (password): the password
        Return:
            true or false
        """

        try:
            user = self._db.find_user_by(email=email)
            hashed = user.hashed_password[2:-1]
            return bcrypt.checkpw(password.encode(), hashed.encode())
        except NoResultFound:
            return False

    def create_session(self, email: str):
        """
        Creates a session id for a user
        Args:
            (email): the user email
        Return:
            newly created session id, None otherwise
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> Union[User, None]:
        """
        Gets user based on their session id
        Args:
            (session_id): the provided session id
        Return:
            the user, otherwise None
        """

        try:
            return self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroys user session"""
        self._db.update_user(user_id, session_id=None)
