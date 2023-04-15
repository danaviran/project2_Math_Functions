#################################################################
# FILE : shapes.py
# WRITER : Dana Aviran , dana.av , 211326608
# EXERCISE : intro2cs2 ex2 2022
#################################################################

import math


def circle_area(r):
    if r > 0:
        return math.pi * r ** 2
    else:
        return None


def rectangle_area(a, b):
    if a > 0 and b > 0:
        return a * b
    else:
        return None


def equilateral_triangle_area(a):
    if a > 0:
        return (math.sqrt(3) / 4) * a ** 2
    else:
        return None


def shape_area():
    x = int(input("Choose shape (1=circle, 2=rectangle, 3=triangle): "))
    if x == 1:
        r = float(input())
        return circle_area(r)
    elif x == 2:
        a = float(input())
        b = float(input())
        return rectangle_area(a, b)
    elif x == 3:
        a = float(input())
        return equilateral_triangle_area(a)
    else:
        return None
