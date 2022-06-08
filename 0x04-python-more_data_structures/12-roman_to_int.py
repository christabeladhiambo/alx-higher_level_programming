#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    sum = 0
    roman_value = {
        "I": 1, "V": 5, "X": 10,
        "L": 50, "C": 100, "D": 500, "M": 1000
    }

    for i in range(len(roman_string)):
        if i < (len(roman_string) - 1) and roman_value.get(
            roman_string[i]
        ) < roman_value.get(roman_string[i + 1]):
            sum -= roman_value.get(roman_string[i])
        else:
            sum += roman_value.get(roman_string[i])
    return sum
