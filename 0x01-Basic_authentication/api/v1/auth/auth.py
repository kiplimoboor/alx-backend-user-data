#!/usr/bin/env python3

"""Authentication Module"""

from typing import List, TypeVar

from flask import request


class Auth:
    """
    An authentication class for REST API
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks whether a path requires authentication or not
        Return:
            True if it requires auth, False otherwise
        """

        if path is None or excluded_paths is None:
            return True
        if path[-1] != '/':
            path += '/'
        if path not in excluded_paths or len(excluded_paths) == 0:
            return True

        return False

    def authorization_header(self, request=None) -> str:
        """
        Checks the authrorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Checks the current user
        Return:
            the User
        """
        return None
