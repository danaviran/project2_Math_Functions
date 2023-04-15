#################################################################
# FILE : temperature.py
# WRITER : Dana Aviran , dana.av , 211326608
# EXERCISE : intro2cs2 ex2 2022
#################################################################


def is_vormir_safe(a, b, c, d):
    a, b, c, d = float(a), float(b), float(c), float(d)
    return (a < b and a < c) or (a < b and a < d) or (a < c and a < d)
