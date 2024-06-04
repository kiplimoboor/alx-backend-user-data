#!/usr/bin/env python3

"""Basic Authentication Module"""

from .auth import Auth


class BasicAuth(Auth):
    """
    A simple basic authentication class
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of Authorization header
        """

        if authorization_header is None or not isinstance(authorization_header, str):
            return None

        header = authorization_header.split()
        if header[0] != "Basic":
            return None
        return header[1]
