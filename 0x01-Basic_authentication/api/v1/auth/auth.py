#!/usr/bin/env python3
"""Auth Module"""
import re
from typing import List, TypeVar
from flask import request


User = TypeVar('User')


class Auth:
    """Authentecation Class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Placeholder method for authentication check """
        return False

    def authorization_header(self, request=None) -> str:
        """ Placeholder method for retrieving authorization header """
        return None

    def current_user(self, request=None) -> User:
        """ Placeholder method for retrieving current user """
        return None
