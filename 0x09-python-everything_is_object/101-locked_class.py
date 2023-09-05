#!/usr/bin/python3
"""Locked Class"""


class LockedClass:
    """Prevents the user from dynamically creating new instance attributes
    Except if the new instance attribute is called first_name.
    """
    def __fixattr__(self, name, value):
        """Fixes the new instance attribute to only be first_name"""
        if name == 'first_name':
            super().__setattr__(name, value)
        raise AttributeError
