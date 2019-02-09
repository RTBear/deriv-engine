#!/usr/bin/python

####################################
# Ryan Mecham
# A01839282
####################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from quot import quot
from ln import ln
from absv import absv
from maker import make_const, make_pwr, make_pwr_expr
import math

def isConstE(c):
    #check if a const is e (2.718...)
    if isinstance(c, const):
        if (c.get_val() - math.e) < .0000001:
            return True

    return False

def const_flatten(c):
    while(type(c) != type(1.0) and type(c) != type(1)):
        c = c.get_val()
    return const(c)

def flattenProduct(prd):

    while type(prd) == type(prod(const(1),const(2))) and type(prd.get_mult2()) == type(prod(const(1),const(2))) and type(prd.get_mult2().get_mult1()) == type(const(1)) and type(prd.get_mult1()) == type(const(1)): #while left is const and right is product with const in first arg
        prd = prod(const(prd.get_mult1().get_val()*prd.get_mult2().get_mult1().get_val()),prd.get_mult2().get_mult2())#combine left

    left = prd.get_mult1()
    right = prd.get_mult2()
    if type(right) == type(const(1)) and type(left) == type(const(1)):
        return const.mult(right,left)

    return prd

def flattenPlus(pls):

    while type(pls) == type(plus(const(1),const(2))) and type(pls.get_elt1()) == type(plus(const(1),const(2))) and type(pls.get_elt2()) == type(const(1)) and type(pls.get_elt1().get_elt2()) == type(const(1)): #pls is plus type and right is const and right of left-side is const
        pls = plus(pls.get_elt1().get_elt1(),const.add(pls.get_elt2(),pls.get_elt1().get_elt2()))

    return pls

def quotToProd(expr):
    assert isinstance(expr, quot), 'must be a quot'
    num = expr.get_num()
    denom = expr.get_denom()
    p = prod(num,pwr(denom,const(-1.0)))
    return p

def deriv(expr):
    if isinstance(expr, const):
        return const_deriv(expr)
    elif isinstance(expr, pwr):
        return pwr_deriv(expr)
    elif isinstance(expr, prod):
        return prod_deriv(expr)
    elif isinstance(expr, plus):
        return plus_deriv(expr)
    elif isinstance(expr, quot):
        return quot_deriv(expr)
    elif isinstance(expr, var):
        return const(1.0)
    elif isinstance(expr, ln):
        return ln_deriv(expr)
    else:
        raise Exception('deriv:' + repr(expr))

# the derivative of a consant is 0.
def const_deriv(c):
    assert isinstance(c, const)
    return const(val=0.0)

def plus_deriv(s):
    left = s.get_elt1()
    right = s.get_elt2()
    return flattenPlus(plus(elt1=deriv(left),elt2=deriv(right)))

def ln_deriv(expr):
    assert isinstance(expr, ln)
    inner = expr.get_expr()
    #f`(ln(g(x))) = g`(x)/g(x)
    return quot(deriv(inner) , inner)


def pwr_deriv(p):
    assert isinstance(p, pwr)
    b = p.get_base()
    d = p.get_deg()
    if isinstance(b, var): #if base is a variable (ie x^2)
        if isinstance(d, const): #no 2^x garbage
            if d.get_val() == 0.0:#x^0
                return make_const(0.0)
            neg1 = make_const(-1.0)
            new_d = const.add(const_flatten(d),neg1)
            
            if new_d.get_val() == 0.0:#TODO: Handle something like x^0 is already 1
                # return d
                # print 'here'
                return const(1.0)
            return flattenProduct(prod(mult1=d,mult2=pwr(b,new_d)))
        else:
            raise Exception('pwr_deriv: case 1: ' + str(p))
    elif isinstance(b, plus) or isinstance(b, prod) or isinstance(b, pwr) or isinstance(b, quot) or isinstance(b, ln): #base is an expression ie: (x + 2)^2 or (2x)^2 etc
        if isinstance(d, const):
            if d.get_val() == 0.0:
                return make_const(0.0)
            neg1 = make_const(-1.0)
            new_d = d.add(const_flatten(d),neg1)
            if new_d.get_val() == 0.0:#TODO: Handle something like x^0 is already 1
                return deriv(b)

            return flattenProduct(prod(mult1=flattenProduct(prod(mult1=d, mult2=pwr(b,new_d))), mult2=deriv(b)))
        else:
            raise Exception('pwr_deriv: case 2: ' + str(p))
    elif isConstE(b):
        if isinstance(d, const):
            #f`(e^c) == 0, where c is a constant
            return make_const(0.0)
        elif isinstance(d, plus) or isinstance(d, prod) or isinstance(d, pwr) or isinstance(d, quot): #base is an expression ie: (x + 2)^2 or (2x)^2 etc
            pass#do stuff
            # d/dx(e^f(x)) = f`(x)*e^f(x)
            return flattenProduct(prod( deriv(d), p )) #where d is f`(x) and p is e^f(x), ie the original expression
        else:
            raise Exception('pwr_deriv: case 2: ' + str(p))
    else:
        raise Exception('power_deriv: case 3: ' + str(p) + ' --type-- ' + str(type(b)))

def quot_deriv(q):
    return prod_deriv(quotToProd(q))

def prod_deriv(p):
    assert isinstance(p, prod)
    m1 = p.get_mult1()
    m2 = p.get_mult2()
    if isinstance(m1, const):# ie: 2 * x
        if isinstance(m2, const):# ie: 2 * 4
            return make_const(0.0)
        elif isinstance(m2, pwr):
            #m1*drv(m2)
            return flattenProduct(prod(m1,deriv(m2)))
        elif isinstance(m2, plus):
            #(f*g)' = f'*g + f*g' but f is a constant so...
            return flattenProduct(prod(m1,deriv(m2)))
        elif isinstance(m2, prod):
            return flattenProduct(prod(m1,deriv(m2)))
        else:
            raise Exception('prod_deriv: case 1' + str(p))
    # elif isinstance(m1, plus):
    elif isinstance(m2, const):
        #(f*g)' = f'*g + f*g' where g' == 0 so (f*g)' = f'*g
        return flattenProduct(prod(m2,deriv(m1)))
    elif isinstance(m1, plus) or isinstance(m1, prod) or isinstance(m1, pwr) or isinstance(m1, quot) or isinstance(m1, var):
        #(f*g)' = f'*g + f*g'
        return plus( flattenProduct(prod(m2,deriv(m1))), flattenProduct(prod(m1,deriv(m2))) ) #full product rule
    else:
       raise Exception('prod_deriv: case 2:' + str(p))



