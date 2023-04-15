#################################################################
# FILE : largest_and_smallest.py
# WRITER : Dana Aviran , dana.av , 211326608
# EXERCISE : intro2cs2 ex2 2022
# EXAMPLE EXPLANATION: first - I wanted to check how does my algorithm
# react to decimal numbers, and if it can handle the evaluation between 0, 0.0
# second - I wanted to check that it can handle negative numbers
#################################################################

import math


def largest(a, b):
    if a >= b:
        return a
    else:
        return b


def lowest(a, b):
    if a <= b:
        return a
    else:
        return b


def largest_and_smallest(a, b, c):
    x = largest(largest(a, b), largest(b, c))
    y = lowest(lowest(a, b), lowest(b, c))
    return x, y


def check_largest_and_smallest():
    x1 = largest_and_smallest(17, 1, 6)[0] == 17 \
            and largest_and_smallest(17, 1, 6)[1] == 1
    x2 = largest_and_smallest(1, 17, 6)[0] == 17 \
            and largest_and_smallest(1, 17, 6)[1] == 1
    x3 = largest_and_smallest(1, 1, 2)[0] == 2 \
            and largest_and_smallest(1, 1, 2)[1] == 1
    x4 = largest_and_smallest(0.0, 0, 0.8)[0] == 0.8 \
            and largest_and_smallest(0.0, 0, 0.8)[1] == 0
    x5 = largest_and_smallest(-8, -9, -10)[0] == -8 \
            and largest_and_smallest(-8, -9, -10)[1] == -10
    return x1 and x2 and x3 and x4 and x5
