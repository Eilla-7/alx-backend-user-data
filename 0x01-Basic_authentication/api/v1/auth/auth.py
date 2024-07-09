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
        if path is not None and excluded_paths is not None:
            for exclusion_path in map(lambda x: x.strip(), excluded_paths):
                guide = ''
                if exclusion_path[-1] == '*':
                    guide = '{}.*'.format(exclusion_path[0:-1])
                elif exclusion_path[-1] == '/':
                    guide = '{}/*'.format(exclusion_path[0:-1])
                else:
                    guide = '{}/*'.format(exclusion_path)
                if re.match(guide, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Placeholder method for retrieving authorization header """
        return None

    def current_user(self, request=None) -> User:
        """ Placeholder method for retrieving current user """
        return None
