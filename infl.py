#!/usr/bin/python

#######################################
# module: infl.py
# Ryan Mecham
# A01839282
#######################################

from const import const
from deriv import deriv
from poly12 import find_poly_1_zeros, find_poly_2_zeros
from tof import tof
from point2d import point2d

def find_infl_pnts(expr):
    drv = deriv(expr)
    drv_2 = deriv(drv)
    # print 'f`(x) = ', drv
    # print 'f``(x) = ', drv_2
    zeros = None
    try:
        zeros = find_poly_1_zeros(drv_2)
        # print '1st degree poly'
    except Exception:
        # print 'not a 1st degree poly'
        pass

    try:
        zeros = find_poly_2_zeros(drv_2)
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
    delta = 0.1
    points = [] #will store array of points and if they are max/min
    #zeros may be None if no inflection points
    if not zeros == None:
        for z in zeros:
            z_val = f(z.get_val())
            z_minus = f_dp(z.get_val() - delta)
            z_plus = f_dp(z.get_val() + delta)
            if z_minus < 0 and z_plus > 0:
                points.append(point2d(z,const(z_val)))
            if z_minus > 0 and z_plus < 0:
                points.append(point2d(z,const(z_val)))
    else:
        return None

    if points == []:
        return None
    else:
        # print points
        return points
    
    
            

    
