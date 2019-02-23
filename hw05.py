#!/usr/bin/python

###########################################
# module: hw05.py
# Ryan Mecham
# A01839282
###########################################

from const import const
from prod import prod
from pwr import pwr
from quot import quot
from ln import ln
from deriv import deriv
from tof import tof
from maker import make_e_expr, make_pwr


import math




###################### Problem 1 ########################

def solve_pdeq(k1, k2):
    assert isinstance(k1, const)
    assert isinstance(k2, const)
    #k1*y` = k2*y
    #y` = (k2/k1) * y
    #let k2/k1 = k
    #y` = k*y
    #therefore y = C*e^(kt) and y` = k*C*e^(kt) or y` = (k2/k1)*C*e^(kt)
    #I am going to let C = 1/k
    #so we get:
    #return e^((k2/k1)*x)
    # return prod(quot(k2,k1), make_e_expr(prod(quot(k2,k1),make_pwr('x',1.0)))) #C = 1
    return make_e_expr(prod(quot(k2,k1),make_pwr('x',1.0))) #C = 1/k

def solve_pdeq_with_init_cond(y0, k):
    assert isinstance(y0, const)
    assert isinstance(k, const)
    #y` = ky
    #y(0) = P_0
    #and
    #y = P(t) = y(0)*e^(kt) = P_0*e^(kt)
    #return y0 * e^(k*x)
    return prod(y0, make_e_expr(prod(k,make_pwr('x',1.0))))

############################ Problem 2 ########################

def find_growth_model(p0, t, n):
    assert isinstance(p0, const)
    assert isinstance(t, const)
    assert isinstance(n, const)

    #p0 is C
    #n  is k
    #t  is t

    return prod(p0,make_e_expr(prod(quot(ln(n),t),make_pwr('t',1))))

############################# Problem 3 ##############################

def radioactive_decay(lmbda, p0, t):
    assert isinstance(lmbda, const)
    assert isinstance(p0, const)
    assert isinstance(t, const)

    #exponential decay is P(t) = p0 * e^(-lambda * t) 
    return prod(p0,make_e_expr(prod(lmbda,make_pwr('t',1))))

############################# Problem 4 ##############################

def c14_carbon_dating(c14_percent):
    assert isinstance(c14_percent, const)
    #decay formula for carbon 14 is P(t) = p0*e^(-0.00012*t)
    #from this we get t = ln(c14_percent)/-0.00012
    #so we get
    return const(math.ceil(math.log(c14_percent.get_val()) / -0.00012))

############################# Problem 5 ##############################

def demand_elasticity(demand_eq, price):
    assert isinstance(price, const)
    # E(p) = (-p*f`(p))/f(p)
    f = tof(demand_eq)
    drv = deriv(demand_eq)
    fprime = tof(drv)
    p = price.get_val()

    return const((-p*fprime(p)) / f(p))

def is_demand_elastic(demand_eq, price):
    assert isinstance(price, const)
    return demand_elasticity(demand_eq, price) > 1.0 #acknowledgement of edge case: demand_elasticity is 1, which is undefined in the lecture notes, but will return False (ie inelastic).
    

def expected_rev_dir(demand_eq, price, price_direction):
    assert isinstance(price, const)
    assert isinstance(price_direction, const)
    assert price_direction.get_val() == 1 or \
           price_direction.get_val() == -1

    f = tof(demand_eq)
    p = price.get_val()
    E_p = demand_elasticity(demand_eq, price).get_val()
    p1 = p + price_direction.get_val()
    E_p_1 = demand_elasticity(demand_eq, const(p1)).get_val()
    #d/dp R(p) = f(p)(1 - E(p))

    rprime_0 = f(p)*(1 - E_p)
    rprime_1 = f(p)*(1 - E_p_1)

    if rprime_0 > rprime_1: #old higher than new
        #will go down
        return const(-1.0)
    elif rprime_1 > rprime_0: #new higher than old
        #will go up
        return const(1.0)
    else:
        #will not change
        return const(0.0)


    
