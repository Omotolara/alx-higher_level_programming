#!/usr/bin/python3
""" MyList class that inherits from list """


class MyList(list):
    """ Defines MyList class """

    def print_sorted(self):
        """ Prints the sorted list n ascending order """
        list_sort = sorted(self)
        print(list_sort)
