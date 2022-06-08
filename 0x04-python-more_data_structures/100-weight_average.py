#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list and not (len(my_list)):
        return 0
    totalScore = 0
    totalWeight = 0
    for elem in my_list:
        score, weight = elem
        totalScore += score * weight
        totalWeight += weight
    return totalScore / totalWeight
