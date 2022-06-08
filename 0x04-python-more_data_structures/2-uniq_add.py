#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq_num = []
    for num in my_list:
        if num not in uniq_num:
            uniq_num.append(num)
    return sum(uniq_num)
