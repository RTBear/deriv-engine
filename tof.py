#!/usr/bin/python


###########################################
# module: tof.py
# Ryan Mecham
# A01839282
###########################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from quot import quot
import math

def tof(expr):
    if isinstance(expr, const):
        return const_tof(expr)
    elif isinstance(expr, pwr):
        return pwr_tof(expr)
    elif isinstance(expr, prod):
        return prod_tof(expr)
    elif isinstance(expr, plus):
        return plus_tof(expr)
    elif isinstance(expr, quot):
        return quot_tof(expr)
    elif isinstance(expr, var):
        return lambda x: x
    else:
        raise Exception('tof: ' + str(expr))

## here is how you can implement converting
## a constant to a function.
def const_tof(c):
    assert isinstance(c, const)
    def f(x):
        return c.get_val()
    return f

def pwr_tof(expr):
    assert isinstance(expr, pwr)
    expb = expr.get_base()
    d = expr.get_deg()
    if isinstance(expb, const):#base is a constant eg 2^3 
        assert isinstance(d, const), "I am currently only considering expressions raised to constants for simplicity"#assuming d is constant

        b_val = expb.get_val()
        d_val = d.get_val()
        return lambda x: b_val**d_val

    elif isinstance(expb, var):
        if isinstance(d, const):
            return lambda x: x ** d.get_val()
        else:
            raise Exception('pw_tof: case 1:' + str(expr))
    elif isinstance(expb, plus) or isinstance(expb, pwr) or isinstance(expb, prod) or isinstance(expb, quot):
        if isinstance(d, const):
            return lambda x: tof(expb)(x) ** d.get_val()
        else:
            raise Exception('pw_tof: case 2:' + str(expr))
    else:
        raise Exception('pw_tof: case 5:' + str(expr))

def quot_tof(expr):
    assert isinstance(expr, quot)
    left = expr.get_num()
    right = expr.get_denom()

    if isinstance(left, const):
        if isinstance(right, const):
            return lambda x: left.get_val() / right.get_val()
        elif isinstance(right, var):
            return lambda x: left.get_val() / x
        elif isinstance(right, plus) or isinstance(right, pwr) or isinstance(right, prod) or isinstance(right, quot):
            return lambda x: left.get_val() / tof(right)(x)
        else:
            raise Exception('prod_tof: case 2:' + str(expr))
    elif isinstance(left, var) or isinstance(left, plus) or isinstance(left, pwr) or isinstance(left, prod) or isinstance(left, quot):
        if isinstance(right, const):
            return lambda x: tof(left)(x) / right.get_val()
        elif isinstance(right, var) or isinstance(right, plus) or isinstance(right, pwr) or isinstance(right, prod) or isinstance(right, quot):
            return lambda x: tof(left)(x) / tof(right)(x)
        else:
            raise Exception('prod_tof: case 3:' + str(expr))
    else:
        raise Exception('prod_tof: case 1:' + str(expr))
def prod_tof(expr):
    assert isinstance(expr, prod)
    left = expr.get_mult1()
    right = expr.get_mult2()

    if isinstance(left, const):
        if isinstance(right, const):
            return lambda x: left.get_val() * right.get_val()
        elif isinstance(right, var):
            return lambda x: left.get_val() * x
        elif isinstance(right, plus) or isinstance(right, pwr) or isinstance(right, prod) or isinstance(right, quot):
            return lambda x: left.get_val() * tof(right)(x)
        else:
            raise Exception('prod_tof: case 2:' + str(expr))
    elif isinstance(left, var) or isinstance(left, plus) or isinstance(left, pwr) or isinstance(left, prod) or isinstance(left, quot):
        if isinstance(right, const):
            return lambda x: tof(left)(x) * right.get_val()
        elif isinstance(right, var) or isinstance(right, plus) or isinstance(right, pwr) or isinstance(right, prod) or isinstance(right, quot):
            return lambda x: tof(left)(x) * tof(right)(x)
        else:
            raise Exception('prod_tof: case 3:' + str(expr))
    else:
        raise Exception('prod_tof: case 1:' + str(expr))

def plus_tof(expr):
    assert isinstance(expr, plus)
    left = expr.get_elt1()
    right = expr.get_elt2()

    if isinstance(left, const):
        if isinstance(right, const):
            return lambda x: left.get_val() + right.get_val()
        elif isinstance(right, var):
            return lambda x: left.get_val() + x
        elif isinstance(right, plus) or isinstance(right, pwr) or isinstance(right, prod) or isinstance(right, quot):
            return lambda x: left.get_val() + tof(right)(x)
        else:
            raise Exception('prod_tof: case 2:' + str(expr))
    elif isinstance(left, var) or isinstance(left, plus) or isinstance(left, pwr) or isinstance(left, prod) or isinstance(left, quot):
        if isinstance(right, const):
            return lambda x: tof(left)(x) + right.get_val()
        elif isinstance(right, var) or isinstance(right, plus) or isinstance(right, pwr) or isinstance(right, prod) or isinstance(right, quot):
            return lambda x: tof(left)(x) + tof(right)(x)
        else:
            raise Exception('prod_tof: case 3:' + str(expr))
    else:
        raise Exception('prod_tof: case 1:' + str(expr))


    
