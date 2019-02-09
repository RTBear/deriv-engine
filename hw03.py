#!/usr/bin/python

#######################################
# module: hw03.py
# Ryan Mecham
# A01839282
#######################################

# place all necessary imports here.
#
# I placed the updated version of maker.py
# Use it as you see fit.
import math
from maker import make_const,make_plus,make_prod,make_pwr,make_pwr_expr,make_3rd_degree_poly,make_2nd_degree_poly
from prod import prod
from pwr import pwr
from var import var
from const import const
from derivtest import loc_xtrm_2nd_drv_test,zeros_for_lambda_range,loc_xtrm_1st_drv_test_lmda
from tof import tof
from deriv import deriv
from poly12 import get_consts_poly_1,get_consts_poly_2

def maximize_revenue(dmnd_eq, constraint=lambda x: x >= 0):#only works on linear demand eqs
    rev = incrementPolyPwrs(dmnd_eq,1)
    rev_drv = deriv(rev)
    # print 'eq:',dmnd_eq
    # print 'rev',rev
    # print 'rev deriv',rev_drv
    rev_drv_f = tof(rev_drv)
    dmnd_f = tof(dmnd_eq)
    rev_f = tof(rev)
    # print 'f(20)',dmnd_f(20)
    # print 'R(20)',rev_f(20)
    # print 'R`(20)',rev_drv_f(20)
    xtrm = loc_xtrm_2nd_drv_test(rev)
    for val in xtrm:
        # print val[0]
        # print val[1]
        x = val[1].get_x().get_val()
        y = val[1].get_y().get_val()

        if(val[0] == 'max' and constraint(x)):
            num_units = const(x)
            revenue = const(y)
            price = const(dmnd_f(x))


    return (num_units,revenue,price)

def incrementPolyPwrs(poly, inc):
    #handles first and second degree polys (ax^2 + bx + c) or (bx+c)
    a,b,c = None,None,None
    try:
        b,c = get_consts_poly_1(poly)
        return make_2nd_degree_poly(a=b,b=c,c=const(0.0))
        # print '1st degree poly'
    except Exception:
        # print 'not a 1st degree poly'
        try:
            a,b,c = get_consts_poly_2(poly)
            return make_3rd_degree_poly(a=a,b=b,c=c,d=const(0.0))
        # print '2nd degree poly'
        except Exception:
        # print 'not a 2nd degree poly'
            raise Exception('incrementPolyPwrs: ' + str(poly))

    

def dydt_given_x_dxdt(yt, x, dxdt):
    # print deriv(yt)
    dydt = tof(deriv(yt))(x.get_val()) * dxdt.get_val()
    return const(dydt)


def oil_disk_test():
    yt = make_prod(make_const(0.02*math.pi),
                    make_pwr('r', 2.0))
    print(yt)
    dydt = dydt_given_x_dxdt(yt, make_const(150.0),
                             make_const(20.0))
    assert not dydt is None
    assert isinstance(dydt, const)
    print(dydt)

def arm_tumor_test():
    yt = make_prod(make_const(0.003*math.pi),
                    make_pwr('r', 3.0))
    print(yt)
    dydt = dydt_given_x_dxdt(yt, make_const(10.3),
                             make_const(-1.75))
    assert not dydt is None
    assert isinstance(dydt, const)
    
    print(dydt)

if __name__ == "__main__":
    oil_disk_test()
    arm_tumor_test()

    
