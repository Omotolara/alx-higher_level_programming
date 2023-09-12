#!/usr/bin/python3
""" Lookup Function """


def lookup(obj):
    """ Returns the list of available attributes and methods of an object"""
    attr_md = dir(obj)
    return attr_md
