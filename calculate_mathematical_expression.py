#################################################################
# FILE : calculate_mathematical_expression.py
# WRITER : Dana Aviran , dana.av , 211326608
# EXERCISE : intro2cs2 ex2 2022
#################################################################

def calculate_mathematical_expression(a, b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return b * a
    elif c == ":":
        if b == 0:
            return None
        else:
            return a / b
    else:
        return None


def calculate_from_string(y):
    x = y.split()
    a = float(x[0])
    b = float(x[2])
    activity = x[1]
    return calculate_mathematical_expression(a, b, activity)