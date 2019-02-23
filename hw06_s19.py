#!/usr/bin/python

#############################################
# module: hw06_s19.py
# YOUR NAME
# YOUR A#
#############################################

# These are the imports I used to implement my 
# solutions. Modify them as you see fit but
# make sure all your imports are zipped in your
# submission.

import math
import numpy as np
import matplotlib.pyplot as plt

from const import const
from maker import make_prod, make_const, make_pwr, make_e_expr, make_plus, make_quot
from ln import ln
from quot import quot
from plus import plus
from prod import prod
from tof import tof
from deriv import deriv

## ************* Problem 1 ******************

def percent_retention_model(lmbda, a):
    assert isinstance(lmbda, const)
    assert isinstance(a, const)

    #r(t) = (100 - a)*e^(-lmda*t) + a
    return plus( prod(plus(const(100.0),prod(const(-1.0),a)) , make_e_expr(prod(prod(const(-1.0),lmbda),make_pwr('t',1)))) , a )

def plot_retention(lmbda, a, t0, t1):
    assert isinstance(lmbda, const)
    assert isinstance(a, const)
    assert isinstance(t0, const)
    assert isinstance(t1, const)
    # your code here
    pass

## ************* Problem 2 ******************

def plot_spread_of_disease(p, t0, p0, t1, p1, tl, tu):
    assert isinstance(p, const) and isinstance(t0, const)
    assert isinstance(p0, const) and isinstance(t1, const)
    # your code here
    pass



def spread_of_disease_model(p, t0, p0, t1, p1):
    assert isinstance(p, const) and isinstance(t0, const)
    assert isinstance(p0, const) and isinstance(t1, const)

    #f(t) = P/(1+B*e^(-c*t))
    #p = 500,000
    #let t0 = 0 such that f(t0) = f(0)
    #this would make t1 = delta_t
    #where delta_t = t1 - t0
    #f(0) = p0 = 200 = 500,000/(1+B*e^0) = 500,000/(1+B) => B = 2499
    #generally: B = (p-p0)/p0
    #f(1) = p1 = 500 = 500,000/(1+2499*e^(-c*1)) => c = .92
    #generally: c = -ln((p-p1)/(p1*B))/t

    #so we get f(t) = p/(1+((p-p0)/p0)*e^(-(-ln((p-p1)/(p1*((p-p0)/p0))))*t))
    #or f(t) = p/(1+((p-p0)/p0)*e^((ln((p-p1)/(p1*((p-p0)/p0)))/(t1-t0)*t))
    #return f(t)
    return quot(p,plus(const(1.0),prod(quot(plus(p,prod(const(-1.0),p0)),p0),make_e_expr(ln(prod(quot(quot(plus(p,prod(const(-1.0),p1)),prod(p1,quot(plus(p,prod(const(-1.0),p0)),p0))),plus(t1,prod(const(-1.0),t0))),make_pwr('t',1)))))))


## ************* Problem 3 ******************

def plot_plant_growth(m, t1, x1, t2, x2, tl, tu):
    assert isinstance(m, const) and isinstance(t1, const)
    assert isinstance(x1, const) and isinstance(t2, const)
    assert isinstance(x2, const) and isinstance(tl, const)
    assert isinstance(tu, const)
    # your code here
    pass

def plant_growth_model(m, t1, x1, t2, x2):
    assert isinstance(m, const) and isinstance(t1, const)
    assert isinstance(x1, const) and isinstance(x2, const)
    assert isinstance(x2, const)

    #B,M,k
    #M is 1000 (maximum population)
    #B is 9 (which is (M-x1)/x1)
    #k is 0.00037 (which is (ln((m-x2)/(x2*B))/(-M*(t2-t1))) )

    #f(t) = M / (1+B*e^(-Mkt)
    #or f(t) = m / (1+((m-x1)/x1)*e^(-Mkt))
    return quot(m,plus(const(1.0),prod(quot(plus(m,prod(const(-1.0),x1)),x1),make_e_expr(prod(prod(prod(const(-1.0),m),quot(ln(plus(m,prod(const(-1.0),x2)),prod(x2,quot(plus(m,prod(const(-1.0),x1)),x1))),prod(prod(const(-1.0),m),plus(t2,prod(const(-1.0),t1))))),make_pwr('t',1))))))
    
                                      
## ************* Problem 4 ******************

def spread_of_news_model(p, k):
    assert isinstance(p, const) and isinstance(k, const)
    #t0 = 4
    #t1 = ?
    #p = .5 * P => P(1 - e^(-k*4)) = .5*P (where t=4) => k = -0.25*ln(0.5) ~= 1.73 => f(t) = P(1 - e^(-1.73*t))
    #p1 = .9 * P (p0 and p1 given)

    #we can now compute t1
    #0.9*P = P(1 - e^(-1.73*t)) => t ~= 13.3
    
    #generally
    #f(t) = P(1-e^(-kt)) we know that f(0) = 0
    #where p0 is initial knowing pop at time t0
    #and p1 is pop at time t1

    #return f(t)
    #where f(t) = p*(1 - e^(-k*t))
    #where k = (1/t0)*ln(p0)
    #so return p*(1 - e^(( -( (1/t0)*ln(p0) ) )*t)) #if given p0 and t0
    #we are given k so:
    #return p*(1 - e^(-k*t))

    return prod(p,plus(1,prod(const(-1.0),make_e_expr(prod(prod(const(-1),k),make_pwr('t',1))))))

def plot_spread_of_news(p, k, tl, tu):
    assert isinstance(p, const) and isinstance(k, const)
    assert isinstance(tl, const) and isinstance(tu, const)
    # your code here
    pass




 
