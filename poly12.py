#!/usr/bin/python

############################################
# module: poly12.py
# Ryan Mecham
# A01839282
############################################

from prod import prod
from const import const
from pwr import pwr
from plus import plus
from var import var
from deriv import deriv
from tof import tof
import math

def get_consts_poly_1(expr):
    #polynomials of degree 1, ie: mx + b
    #since expr will be linear, we know it will only ever return a single zero
    assert isinstance(expr, plus), 'expression must be of form mx+b'

    left = expr.get_elt1()
    right = expr.get_elt2()
    m = None
    b = None

    if isinstance(left, pwr): #of form x^1 + b
        if isinstance(right, const):
            m = const(1.0)
            b = right
        else:
            raise Exception('find_poly_1_zeros: case 1: ' + str(expr))
    elif isinstance(left, prod):
        l_left = left.get_mult1()
        l_right = left.get_mult2()

        if isinstance(l_left, pwr): #of form x^1*m + b :(
            if isinstance(l_right, const):
                m = l_right 
                b = right
            else:
                raise Exception('find_poly_1_zeros: case 3: ' + str(expr))
        elif isinstance(l_right, pwr): #of form m*x^1 + b
            if isinstance(l_left, const):
                m = l_left
                b = right
            else:
                raise Exception('find_poly_1_zeros: case 4: ' + str(expr))
        else:
            raise Exception('find_poly_1_zeros: case 5: ' + str(expr))
    else:
        raise Exception('find_poly_1_zeros: case 6: ' + str(expr))

    assert not m == None
    assert not b == None

    return (m,b)

def getConstFromPwr(expr):
    if isinstance(expr, pwr):
        return const(1.0)
    elif isinstance(expr, prod):
        left = expr.get_mult1()
        right = expr.get_mult2()
        if isinstance(left, const):
            return left
        elif isinstance(right, const):
            return right
        else:
            raise Exception('getConstFromPwr: case 2: ' + str(expr))
    else:
        raise Exception('getConstFromPwr: case 1: ' + str(expr))

def get_consts_poly_2(expr):
    #polynomials of degree 2, ie: ax^2 + bx^1 + c
    #polynomials of degree 1, ie: mx + b
    #since expr will be linear, we know it will only ever return a single zero
    assert isinstance(expr, plus), 'expression must be of form ax^2 + bx^1 + c'

    left = expr.get_elt1()
    right = expr.get_elt2()

    a = None
    b = None
    c = None

    #cases that are considered are:
    #of form x^2 + (bx^1 + c)   DONE
    #of form ax^2 + (bx^1 + c)  DONE
    #of form ax^2 + (x^1 + c)   DONE

    #of form (ax^2 + bx^1) + c  DONE
    #of form (x^2 + bx^1) + c   DONE
    #of form (ax^2 + x^1) + c   DONE
    #of form (x^2 + x^1) + c    DONE

    if isinstance(left, pwr): #of form x^2 + (bx^1 + c)
        if isinstance(right, plus): #RIGHT
            a = const(1.0)
            b,c = get_consts_poly_1(right)
        else:
            raise Exception('find_poly_2_zeros: case 1: ' + str(expr))
    elif isinstance(left, prod): #of form ax^2 + (bx^1 + c) or of form ax^2 + (x^1 + c)
        # left = flattenProduct(left)
        a = getConstFromPwr(left)
        b,c = get_consts_poly_1(right)
    elif isinstance(left, plus):
        #of form (ax^2 + bx^1) + c  
        #of form (x^2 + bx^1) + c   
        #of form (ax^2 + x^1) + c
        #of form (x^2 + x^1) + c
        ################################################################################

        assert isinstance(right, const)

        l_left = left.get_elt1()
        l_right = left.get_elt2()

        a = getConstFromPwr(l_left)
        b = getConstFromPwr(l_right)
        c = right

        ################################################################################
    else:
        raise Exception('find_poly_2_zeros: case 6: ' + str(expr))

    assert not a == None
    assert not b == None
    assert not c == None
    
    return (a,b,c)
    
    
            
def find_poly_1_zeros(expr):
    m,b = get_consts_poly_1(expr)
    zero = const.divide(const.mult(const(-1.0), b), m)
    return zero

def find_poly_2_zeros(expr):
    a,b,c = get_consts_poly_2(expr)
    # print a,b,c

    a_c = a.get_val()
    b_c = b.get_val()
    c_c = c.get_val()

    sq = math.sqrt((b_c ** 2) - (4*a_c*c_c))
    z_minus = (-b_c - sq) / (2*a_c)
    z_plus = (-b_c + sq) / (2*a_c)
    # print 'minus',z_minus
    # print 'plus',z_plus
    # print '----',abs(z_minus - z_plus)

    zeros = [const(z_minus)]
    if abs(z_minus - z_plus) > .000001: #z_minus != z_plus
        zeros.append(const(z_plus))
    else:
        # print '+- zeros are the same (only returning one of them)'
        pass

    return zeros




