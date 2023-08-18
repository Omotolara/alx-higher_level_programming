#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_add = 0
    for element in set(my_list):
        uniq_add += element
    return uniq_add
