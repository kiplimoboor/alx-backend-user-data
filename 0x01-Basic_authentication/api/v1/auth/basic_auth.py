#!/usr/bin/env python3

"""Basic Authentication Module"""

import base64

from .auth import Auth


class BasicAuth(Auth):
    """
    A simple basic authentication class
    """

    def extract_base64_authorization_header(self, auth_header: str) -> str:
        """
        Extracts the Base64 part of Authorization header
        """

        if auth_header is None or not isinstance(auth_header, str):
            return None

        header = auth_header.split()
        if header[0] != "Basic":
            return None
        return header[1]

    def decode_base64_authorization_header(self, b64_auth_header: str) -> str:
        """
        Decodes the extracted base 64 header
        Args:
            b64_auth_header: the base64 header to be decoded
        Return:
            decoded base64 header as utf string, None otherwise
        """

        if b64_auth_header is None or not isinstance(b64_auth_header, str):
            return None

        try:
            return base64.b64decode(b64_auth_header).decode("utf-8")
        except BaseException:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """
        Extracts user credentials from decoded auth header
        Args:
            decoded_base_64_authorization_header: the header with credentials
        Return:
            a tuple with user and pass, None otherwise

        """
        if decoded_base64_authorization_header is None\
                or not isinstance(decoded_base64_authorization_header, str)\
                or ':' not in decoded_base64_authorization_header:
            return (None, None)

        credentials = decoded_base64_authorization_header.split(':')
        return (credentials[0], credentials[1])
