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
from absv import absv
from ln import ln
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
    elif isinstance(expr, absv):
        return absv_tof(expr)
    elif isinstance(expr, ln):
        return ln_tof(expr)
    elif isinstance(expr, var):
        return lambda x: x
    else:
        raise Exception('tof: ' + str(expr))

def is_valid_non_const_var_expr(expr):
    return isinstance(expr, plus) or isinstance(expr, pwr) or isinstance(expr, prod) or isinstance(expr, quot) or isinstance(expr, ln) or isinstance(expr, absv)

def is_valid_non_const_expr(expr):
    return isinstance(expr, var) or isinstance(expr, plus) or isinstance(expr, pwr) or isinstance(expr, prod) or isinstance(expr, quot) or isinstance(expr, ln) or isinstance(expr, absv)

## here is how you can implement converting
## a constant to a function.
def const_tof(c):
    assert isinstance(c, const)
    def f(x):
        return c.get_val()
    return f

def absv_tof(expr):
    inner = expr.get_expr()
    return lambda x: abs(tof(inner)(x))

def ln_tof(expr):
    assert isinstance(expr, ln)
    inner = expr.get_expr()
    # print(tof(inner)(15))
    # print(math.log(0))
    return lambda x: math.log(tof(inner)(abs(x)))

def pwr_tof(expr):
    assert isinstance(expr, pwr)
    expb = expr.get_base()
    d = expr.get_deg()
    if isinstance(expb, const):#base is a constant eg 2^3 
        if isinstance(d, const):
            b_val = expb.get_val()
            d_val = d.get_val()
            return lambda x: b_val**d_val
        else:#may want to be more specific on what is allowed...
            b_val = expb.get_val()
            return lambda x: b_val**tof(d)(x)

    elif isinstance(expb, var):
        if isinstance(d, const):
            return lambda x: x ** d.get_val()
        else:
            raise Exception('pw_tof: case 1:' + str(expr))
    elif is_valid_non_const_var_expr(expb):
        if isinstance(d, const):
            return lambda x: tof(expb)(x) ** d.get_val()
        else:
            raise Exception('pw_tof: case 2:' + str(expr))
    else:
        raise Exception('pw_tof: case 3:' + str(expr))

def quot_tof(expr):
    assert isinstance(expr, quot)
    left = expr.get_num()
    right = expr.get_denom()

    if isinstance(left, const):
        if isinstance(right, const):
            return lambda x: left.get_val() / right.get_val()
        elif isinstance(right, var):
            return lambda x: left.get_val() / x
        elif is_valid_non_const_var_expr(right):
            return lambda x: left.get_val() / tof(right)(x)
        else:
            raise Exception('quot_tof: case 2:' + str(expr))
    elif is_valid_non_const_expr(left):
        if isinstance(right, const):
            return lambda x: tof(left)(x) / right.get_val()
        elif is_valid_non_const_expr(right):
            return lambda x: tof(left)(x) / tof(right)(x)
        else:
            print('here')
            print(type(expr))
            print('left')
            print(type(left))
            print('right')
            print(type(right))
            raise Exception('quot_tof: case 3:' + str(expr))
    else:
        raise Exception('quot_tof: case 1:' + str(expr))
def prod_tof(expr):
    assert isinstance(expr, prod)
    left = expr.get_mult1()
    right = expr.get_mult2()

    if isinstance(left, const):
        if isinstance(right, const):
            return lambda x: left.get_val() * right.get_val()
        elif isinstance(right, var):
            return lambda x: left.get_val() * x
        elif is_valid_non_const_var_expr(right):
            return lambda x: left.get_val() * tof(right)(x)
        else:
            raise Exception('prod_tof: case 2:' + str(expr))
    elif is_valid_non_const_expr(left):
        if isinstance(right, const):
            return lambda x: tof(left)(x) * right.get_val()
        elif is_valid_non_const_expr(right):
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
        elif is_valid_non_const_var_expr(right):
            return lambda x: left.get_val() + tof(right)(x)
        else:
            raise Exception('plus_tof: case 2:' + str(expr))
    elif is_valid_non_const_expr(left):
        if isinstance(right, const):
            return lambda x: tof(left)(x) + right.get_val()
        elif is_valid_non_const_expr(right):
            return lambda x: tof(left)(x) + tof(right)(x)
        else:
            raise Exception('plus_tof: case 3:' + str(expr))
    else:
        raise Exception('plus_tof: case 1:' + str(expr))


    
