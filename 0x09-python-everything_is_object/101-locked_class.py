#!/usr/bin/python3
"""Locked Class"""


class LockedClass:
    """Prevents the user from dynamically creating new instance attributes
    Except if the new instance attribute is called first_name.
    """
    __slots__ = ["first_name"]
