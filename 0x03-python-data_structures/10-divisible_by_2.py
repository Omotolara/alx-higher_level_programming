#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    mult_of_2_list = []
    for element in my_list:
        if element % 2 == 0:
            mult_of_2_list.append(True)
        else:
            mult_of_2_list.append(False)
    return mult_of_2_list
