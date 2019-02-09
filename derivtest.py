#!/usr/bin/python

#########################################
# module: derivtest.py
# Ryan Mecham
# A01839282
#########################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from deriv import deriv
from poly12 import find_poly_1_zeros
from poly12 import find_poly_2_zeros
from tof import tof
from point2d import point2d
import numpy as np


def loc_xtrm_1st_drv_test(expr):
    drv = deriv(expr)
    # print 'f`(x) = ', drv
    zeros = None
    try:
        zeros = find_poly_1_zeros(drv)
        # print '1st degree poly'
    except Exception:
        # print 'not a 1st degree poly'
        pass

    try:
        zeros = find_poly_2_zeros(drv)
        # print '2nd degree poly'
    except Exception:
        # print 'not a 2nd degree poly'
        pass


    if isinstance(zeros,const):
        zeros = [zeros]

    # print 'zeros:'
    # for z in zeros:
    #     print ':',z.get_val()

    f = tof(expr)
    delta = 0.1
    points = [] #will store array of points and if they are max/min
    for z in zeros:
        z_val = f(z.get_val())
        z_minus = f(z.get_val() - delta)
        z_plus = f(z.get_val() + delta)
        if z_minus < z_val and z_plus < z_val:
            points.append(('max',point2d(z,const(z_val))))
        if z_minus > z_val and z_plus > z_val:
            points.append(('min',point2d(z,const(z_val))))
    if points == []:
        return None
    else:
        # print points
        return points

def loc_xtrm_2nd_drv_test(expr):
    drv = deriv(expr)
    drv_2 = deriv(drv)
    # print 'f`(x) = ', drv
    # print 'f``(x) = ', drv_2
    zeros = None
    try:
        zeros = find_poly_1_zeros(drv)
        # print '1st degree poly'
    except Exception:
        # print 'not a 1st degree poly'
        pass

    try:
        zeros = find_poly_2_zeros(drv)
        # print '2nd degree poly'
    except Exception:
        # print 'not a 2nd degree poly'
        pass


    if isinstance(zeros,const):
        zeros = [zeros]
    
    # print 'zeros:'
    # for z in zeros:
    #     print ':',z.get_val()

    f = tof(expr)
    f_dp = tof(drv_2)
    points = [] #will store array of points and if they are max/min
    for z in zeros:
        z_val = f(z.get_val())
        z_f_dp = f_dp(z.get_val())
        if z_f_dp < 0:
            points.append(('max',point2d(z,const(z_val))))
        if z_f_dp > 0:
            points.append(('min',point2d(z,const(z_val))))
    if points == []:
        return None
    else:
        # print points
        return points

def loc_xtrm_1st_drv_test_lmda(expr,rng):

    zeros = zeros_for_lambda_range(tof(deriv(expr)),rng)
    print('zeros',zeros)

    print "expr:",expr
    f = tof(expr)

    delta = 0.1
    points = [] #will store array of points and if they are max/min
    for z in zeros:
        z_val = f(z)
        z_minus = f(z - delta)
        z_plus = f(z + delta)
        if z_minus < z_val and z_plus < z_val:
            points.append(('max',point2d(z,const(z_val))))
        if z_minus > z_val and z_plus > z_val:
            points.append(('min',point2d(z,const(z_val))))
    if points == []:
        return None
    else:
        # print points
        return points

def zeros_for_lambda_range(lmda, rng):
    lambda_x_range = np.linspace(rng[0],rng[1],100000)
    
    zeros = [abs(lmda(x)) < .001 for x in lambda_x_range]
    z = [(float(i) / len(lambda_x_range))*rng[1] for i, zero in enumerate(zeros) if zero == True]
    print z
    for i,val in enumerate(z):
        # print round(val)
        # print abs(round(val) - val)
        if abs(round(val) - val) < .001:
            z[i] = int(round(val))
    print z
    return z
