#################################################################
# FILE : quadratic_equation.py
# WRITER : Dana Aviran , dana.av , 211326608
# EXERCISE : intro2cs2 ex2 2022
# DESCRIPTION: some functions that print math elements
# WEB PAGES I USED: https://stackoverflow.com/questions/15398427/
# solving-quadratic-equation
#################################################################


import math


def quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None, None
    elif discriminant == 0:
        return -b / (2*a), None
    else:
        x1 = (-b + math.sqrt(discriminant)) / 2*a
        x2 = (-b - math.sqrt(discriminant)) / 2*a
        return x1, x2


def quadratic_equation_user_input():
    x = input("Insert coefficients a, b, and c: ")
    x = x.split()  # i need to check if i can use it
    a, b, c = float(x[0]), float(x[1]), float(x[2])
    if a == 0:
        print("The parameter 'a' may not equal 0")
    else:
        x1 = quadratic_equation(a, b, c)[0]
        x2 = quadratic_equation(a, b, c)[1]
        if x1 is None:
            print("The equation has no solutions")
        elif x2 is None:
            print("The equation has 1 solution:", x1)
        else:
            print("The equation has 2 solutions:", x1, "and", x2)

