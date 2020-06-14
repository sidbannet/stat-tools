"""Math operation module.

This module provides library of mathematical operation functions.

NAME
    math
FUNCTIONS
    multiply

@author: siddhartha.banerjee [sidban@uwalumni.com]
"""


def multiply(*args):
    """Method to multiply all input arguments.

    Typical Usage
    =============
    out = multiply(x1, x2, x3, ...)

    :parameter
    x1, x2, x3, ...: is *args with individual arguments either int or float

    :returns
    out: Calculation output of multiplication of all arguments in int or float
    """
    product = 1.0
    for item in args:
        product *= item
    return product


def add(*args):
    """Method to add all input arguments.

    Typical Usage
    =============
    out = add(x1, x2, x3, ...)

    :parameter
    x1, x2, x3, ...: is *args with individual arguments either int or float

    :returns
    out: Calculation output of addition of all arguments in int or float
    """
    total = 0.0
    for item in args:
        total += item
    return total
