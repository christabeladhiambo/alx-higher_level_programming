#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        for key, value_ in a_dictionary.items():
            if value_ == value:
                a_dictionary.pop(key)
                break
    return a_dictionary
