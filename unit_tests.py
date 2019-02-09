#!/usr/bin/python
# -*- coding: utf-8 -*-

#############################################################
# module: unit_tests.py
# description: unit tests for CS 3430: S19: Assignment 01
# bugs to vladimir kulyukin via canvas
##############################################################

from __future__ import print_function
import unittest
import math
from prod import prod
from maker import make_const, make_pwr, make_prod, make_plus, make_point2d, make_quot, make_pwr_expr, make_e_expr, make_ln, make_absv
from plus import plus
from tof import tof
from const import const
from deriv import deriv, logdiff
from poly12 import find_poly_1_zeros, find_poly_2_zeros
from point2d import point2d
from derivtest import loc_xtrm_1st_drv_test, loc_xtrm_2nd_drv_test
from infl import find_infl_pnts
from hw03 import maximize_revenue,dydt_given_x_dxdt
# from graphdrv import graph_drv

class Assign01UnitTests(unittest.TestCase):

    def test_assgn_01_ut_01(self):
        print('\n***** Assign 01: Unit Test 01 ************')
        fex = prod(mult1=make_const(6.0),
                   mult2=make_pwr('x', 3.0))
        drv = deriv(fex)
        assert not drv is None
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 18*(x**2)
        err = 0.00001
        for i in range(1, 100):
            assert abs(drvf(i) - gt(i)) <= err
        print('Assign 01: Unit Test 01: pass')

    def test_assgn_01_ut_02(self):
        print('\n***** Assign 01: Unit Test 02 ************')
        fex = prod(mult1=make_const(3.0),
                   mult2=make_pwr('x', 1.0/3.0))
        drv = deriv(fex)
        assert not drv is None
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: (x**(-2.0/3.0))
        err = 0.00001
        for i in range(1, 100):
            assert abs(drvf(i) - gt(i)) <= err
        print('Assign 01: Unit Test 02: pass')

    def test_assgn_01_ut_03(self):
        print('\n***** Assign 01: Unit Test 03 ************')
        prd = prod(mult1=make_const(2.0), mult2=make_pwr('x', 5.0))
        drv = deriv(prd)
        assert not drv is None
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 10*x**4
        err = 0.00001
        for i in range(-100, 100):
            assert abs(drvf(i) - gt(i)) <= err
        print('Assign 01: Unit Test 03: pass')

    def test_assgn_01_ut_03_1(self):
        print('\n***** Assign 01: Unit Test 03-1 ************')
        prd = prod(mult1=make_const(2.0), mult2=make_pwr('x', 1.0))
        drv = deriv(prd)
        assert not drv is None
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 2*x**0
        err = 0.00001
        for i in range(-100, 100):
            assert abs(drvf(i) - gt(i)) <= err
        # print(prd)
        # print(drv)
        print('Assign 01: Unit Test 03-1: pass')

    def test_assgn_01_ut_04(self):
        print('\n***** Assign 01: Unit Test 04 ************')
        prd = prod(mult1=make_const(-3.0), mult2=make_pwr('x', -1.0))
        drv = deriv(prd)
        assert not drv is None
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 3.0*(x**(-2))
        err = 0.00001
        for i in range(-100, 0):
            assert abs(drvf(i) - gt(i)) <= err
        for i in range(1, 100):
            assert abs(drvf(i) - gt(i)) <= err
        print('Assign 01: Unit Test 04: pass')

    def test_assgn_01_ut_05(self):
        print('\n***** Assign 01: Unit Test 05 ************')
        fex1 = make_pwr('x', 3.0)
        fex2 = prod(mult1=make_const(5.0),
                    mult2=make_pwr('x', 1.0))
        p = plus(elt1=fex1, elt2=fex2)
        drv = deriv(p)
        assert not drv is None
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 3.0*(x**2) + 5.0
        err = 0.00001
        for i in range(-100, 100):
            assert abs(drvf(i) - gt(i)) <= err
        print('Assign 01: Unit Test 05: pass')

    def test_assgn_01_ut_06(self):
        print('\n***** Assign 01: Unit Test 06 ************')
        fex1 = prod(mult1=make_const(2.0),
                    mult2=make_pwr('x', 7.0))
        fex2 = plus(elt1=prod(mult1=make_const(-1.0),
                              mult2=make_pwr('x', 5.0)),
                    elt2=make_const(8.0))
        p = plus(elt1=fex1, elt2=fex2)
        drv = deriv(p)
        assert not drv is None
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 14.0*(x**6) - 5.0*(x**4)
        err = 0.00001 
        for i in range(-100, -1):
            assert abs(drvf(i) - gt(i)) <= err
        for i in range(1, 100):
            assert abs(drvf(i) - gt(i)) <= err
        print('Assign 01: Unit Test 06: pass')

    # def test_assgn_01_ut_001(self):
    #     print('\n***** Assign 01: Unit Test 001 ************')
    #     prd = prod(mult1=make_const(2.0),
    #                mult2=make_pwr('x', 5.0))
    #     # graph_drv(prd, [-3.0, 3.0], [-50, 50.0])
    #     print('Assign 01: Unit Test 01: pass')
    
    # def test_assgn_01_ut_002(self):
    #     print('\n***** Assign 01: Unit Test 002 ************')
    #     fex1 = make_pwr('x', 4.0)
    #     fex2 = make_pwr('x', 3.0)
    #     fex3 = make_pwr('x', 1.0)
    #     fex4 = plus(elt1=fex1, elt2=fex2)
    #     fex5 = plus(elt1=fex4, elt2=fex3)
    #     # graph_drv(fex5, [-2.5, 2.5], [-10.0, 10.0])
    #     print('Assign 01: Unit Test 02: pass')

    # def test_assgn_01_prob_02_ut_03(self):
    #     print('\n***** Assign 01: Unit Test 03 ************')
    #     fex1 = prod(mult1=make_const(-1.0),
    #                 mult2=make_pwr('x', 2.0))
    #     fex2 = plus(elt1=fex1, elt2=make_const(2.0))
    #     # graph_drv(fex2, [-10, 10], [-50.0, 25.0])
    #     print('Assign 01: Unit Test 03: pass')

    # def test_assgn_01_prob_02_ut_04(self):
    #     print('\n***** Assign 01: Unit Test 04 ************')
    #     fex1 = prod(mult1=make_const(2),
    #                 mult2=make_pwr('x', 2.0))
    #     fex2 = plus(elt1=fex1, elt2=make_const(2.0))
    #     # graph_drv(fex2, [-10, 10], [-50.0, 50.0])
    #     print('Assign 01: Unit Test 04: pass')

    def test_assgn_02_prob_01_ut_01(self):
        print('\n***** Assign 02: Unit Test 01 ************')
        f1 = make_prod(make_const(3.0),make_pwr('x', 1.0))
        f2 = make_plus(f1, make_const(100.0))
        z = find_poly_1_zeros(f2)
        f2f = tof(f2)
        assert f2f(z.get_val()) == 0.0
        print('Assign 02: Unit Test 01: pass')

    def test_assgn_02_prob_01_ut_02(self):
        print('\n***** Assign 02: Unit Test 02 ************')
        f0 = make_prod(make_const(0.5), make_pwr('x', 2.0))
        f1 = make_prod(make_const(6.0), make_pwr('x', 1.0))
        f2 = make_plus(f0, f1)
        poly = make_plus(f2, make_const(0.0))
        zeros = find_poly_2_zeros(poly)
        pf = tof(poly)
        for c in zeros:
            assert abs(pf(c.get_val()) - 0.0) <= 0.0001
        print('Assign 02: Unit Test 02: pass')

    def test_assgn_02_prob_02_ut_01(self):
        print('\n***** Assign 02: Unit Test 03 ************')
        f1 = make_prod(make_const(1.0/3.0), make_pwr('x', 3.0))
        f2 = make_prod(make_const(-2.0), make_pwr('x', 2.0))
        f3 = make_prod(make_const(3.0), make_pwr('x', 1.0))
        f4 = make_plus(f1, f2)
        f5 = make_plus(f4, f3)
        poly = make_plus(f5, make_const(1.0))
        xtrma = loc_xtrm_1st_drv_test(poly)
        assert xtrma[0][0] == 'max'
        epsilon = .0001
        assert abs(xtrma[0][1].get_x().get_val() - 1) < epsilon
        assert abs(xtrma[0][1].get_y().get_val() - 2.3333333) < epsilon
        assert abs(xtrma[1][1].get_x().get_val() - 3) < epsilon
        assert abs(xtrma[1][1].get_y().get_val() - 1) < epsilon
        xtrma[0][1]
        assert xtrma[1][0] == 'min'
        print('Assign 02: Unit Test 03: pass')

    def test_assgn_02_prob_02_ut_02(self):
        print('\n***** Assign 02: Unit Test 04 ************')
        f1 = make_prod(make_const(27.0), make_pwr('x', 3.0))
        f2 = make_prod(make_const(-27.0), make_pwr('x', 2.0))
        f3 = make_prod(make_const(9.0), make_pwr('x', 1.0))
        f4 = make_plus(f1, f2)
        f5 = make_plus(f4, f3)
        f6 = make_plus(f5, make_const(-1.0))
        # print('f(x) = ', f6)
        drv = deriv(f6)
        assert not drv is None
        # print('f\'(x) = ', drv)
        xtrma = loc_xtrm_1st_drv_test(f6)
        assert xtrma is None
        print('Assign 02: Unit Test 04: pass')
    
    def test_assgn_02_prob_02_ut_02_1(self):
        print('\n***** Assign 02: Unit Test 05 ************')
        f1 = make_prod(make_const(27.0), make_pwr('x', 3.0))
        f2 = make_prod(make_const(-27.0), make_pwr('x', 2.0))
        f3 = make_prod(make_const(9.0), make_pwr('x', 1.0))
        f4 = make_plus(f1, f2)
        f5 = make_plus(f4, f3)
        f6 = make_plus(f5, make_const(-1.0))
        # print('f(x) = ', f6)
        drv = deriv(f6)
        assert not drv is None
        # print('f\'(x) = ', drv)
        xtrma = loc_xtrm_2nd_drv_test(f6)
        assert xtrma is None
        print('Assign 02: Unit Test 05: pass')

    def test_assgn_02_prob_02_ut_03(self):
        print('\n***** Assign 02: Unit Test 06 ************')
        f1 = prod(mult1=make_const(1.0/4.0),
        mult2=make_pwr('x', 2.0))
        f2 = prod(mult1=make_const(-1.0),
        mult2=make_pwr('x', 1.0))
        f3 = plus(elt1=f1, elt2=f2)
        f4 = plus(elt1=f3, elt2=make_const(2.0))
        # print(f4)
        xtrma = loc_xtrm_2nd_drv_test(f4)
        # for i, j in xtrma:
        #     print(i, str(j))
        assert len(xtrma) == 1 and \
        xtrma[0][1].get_x().get_val() == 2.0 and \
        xtrma[0][1].get_y().get_val() == 1.0
        print('Assign 02: Unit Test 06: pass')

    def test_assgn_02_prob_03_ut_01(self):#test for inflection points
        print('\n***** Assign 02: Unit Test 07 ************')
        f1 = make_pwr('x', 3.0)
        f2 = make_prod(make_const(-3.0), make_pwr('x', 2.0))
        f3 = make_plus(f1, f2)
        f4 = make_plus(f3, make_prod(make_const(0.0), make_pwr('x', 1.0)))
        poly = make_plus(f4, make_const(5.0))
        # print(poly)
        infls = find_infl_pnts(poly)
        epsilon = .0001
        assert abs(infls[0].get_x().get_val() - 1) < epsilon
        assert abs(infls[0].get_y().get_val() - 3) < epsilon
        # for ip in infls:
            # print(str(ip))
        print('Assign 02: Unit Test 07: pass')

    def test_assgn_03_prob_01_ut_01_0(self):
        print('\n***** Assign 03: Unit Test 01 ************')
        e1 = make_plus(make_pwr('x', 1.0), make_const(1.0))
        e2 = make_pwr('x', 3.0)
        e3 = make_prod(make_const(5.0), make_pwr('x', 1.0))
        e4 = make_plus(e2, e3)
        e5 = make_plus(e4, make_const(2.0))
        e6 = make_prod(e1, e5)
        # 1) print the expression we just constructed
        # print('-- function expression is:\n')
        # print(e6)
        # 2) differentiate and make sure that it not None
        drv = deriv(e6)
        assert not drv is None
        # print('-- derivative is:\n')
        # print(e6)
        # 3) convert drv into a function
        e6f = tof(drv)
        assert not e6f is None
        # steps 2) and 3) can be combined into tof(deriv(e6)).
        # 4) construct the ground truth function
        gt = lambda x: 4.0*(x**3) + 3*(x**2) + 10.0*x + 7.0
        # 5) compare the ground truth with what we got in
        # step 3) on an appropriate number range.
        err = 0.00001
        for i in range(10):
            # print(e6f(i), gt(i))
            assert abs(e6f(i) - gt(i)) <= err
        print('Assign 03: Unit Test 01: pass')

    def test_assgn_03_prob_01_ut_02_0(self):
        print('\n***** Assign 03: Unit Test 02 ************')
        e1 = make_prod(make_const(2.0), make_pwr('x', 4.0))
        e2 = make_prod(make_const(-1.0), make_pwr('x', 1.0))
        e3 = make_plus(e1, e2)
        e4 = make_plus(e3, make_const(1.0))
        e5 = make_prod(make_const(-1.0), make_pwr('x', 5.0))
        e6 = make_plus(e5, make_const(1.0))
        e7 = make_prod(e4, e6)
        # print('-- function expression is:\n')
        # print(e7)
        drv = deriv(e7)
        assert not drv is None
        # print('\n-- derivative is:\n')
        # print(drv)
        e7f = tof(drv)
        assert not e7f is None
        gt = lambda x: -18.0*(x**8) + 6.0*(x**5) - 5.0*(x**4) + 8.0*(x**3) - 1.0
        err = 0.00001
        # print('\n--comparison with ground truth:\n')
        for i in range(10):
            # print(e7f(i), gt(i))
            assert abs(e7f(i) - gt(i)) <= err
        print('Assign 03: Unit Test 02: pass')

    def test_assgn_03_prob_01_ut_03_0(self):
        print('\n***** Assign 03: Unit Test 03 ************')
        q = make_quot(make_plus(make_pwr('x', 1.0),
        make_const(11.0)),
        make_plus(make_pwr('x', 1.0), make_const(-3.0)))
        pex = make_pwr_expr(q, 3.0)
        # print('-- function expression is:\n')
        # print(pex)
        pexdrv = deriv(pex)
        assert not pexdrv is None
        # print('\n-- derivative is:\n')
        # print(pexdrv)
        pexdrvf = tof(pexdrv)
        assert not pexdrvf is None
        gt = lambda x: -42.0*(((x + 11.0)**2)/((x - 3.0)**4))
        err = 0.00001
        # print('\n--comparison with ground truth:\n')
        for i in range(10):
            if i != 3.0:
                # print(pexdrvf(i), gt(i))
                assert abs(pexdrvf(i) - gt(i)) <= err
        print('Assign 03: Unit Test 03: pass')

    def test_assgn_03_prob_02_ut_01_0(self):
        print('\n***** Assign 03: Unit Test 04 ************')
        e1 = make_prod(make_const(1.0/12.0), make_pwr('x', 2.0))
        e2 = make_prod(make_const(-10.0), make_pwr('x', 1.0))
        sum1 = make_plus(e1, e2)
        sum2 = plus(sum1,make_const(300.0))
        # drv = deriv(sum2)
        # print sum2
        # print drv
        xtrm = loc_xtrm_2nd_drv_test(sum2)
        # for val in xtrm:
        #     print(val[0])
        #     print(val[1])
        # print loc_xtrm_2nd_drv_test(drv)
        num_units, rev, price = maximize_revenue(dmnd_eq=sum2,constraint=lambda x: 0 <= x <= 60)
        # print "num_units",num_units
        # print 'rev',rev
        # print 'price',price
        err = .001
        assert abs(num_units.get_val() - 20.0) < err
        assert abs(rev.get_val() - 2666.6666666) < err
        assert abs(price.get_val() - 133.33333333) < err
        print('Assign 03: Unit Test 04: pass')

    def test_assgn_03_prob_03_ut_01_0(self):
        print('\n***** Assign 03: Unit Test 05 ************')
        yt = make_prod(make_const(0.02*math.pi), make_pwr('r', 2.0))
        # print(yt)
        dydt = dydt_given_x_dxdt(yt, make_const(150.0),make_const(20.0))
        assert not dydt is None
        assert isinstance(dydt, const)
        assert abs(dydt.get_val() - 376.991118431) < .001
        print('Assign 03: Unit Test 05: pass')
    
    ##########################################################
    #grading unit tests for assign 3
    ##########################################################

    def test_assign_03_prob_01_ut_01(self):
        print('\n***** Assign 03: Problem 01: Unit Test 01 *****')
        e1 = make_pwr('x', 2.0)
        e2 = make_pwr('x', 3.0)
        e3 = make_prod(e1, e2)
        # print(e3)
        drv = deriv(e3)
        assert not drv is None
        # print(drv)
        e3f = tof(drv)
        assert not e3f is None
        f = lambda x: 5.0*(x**4)
        err = 0.0001
        for i in range(10):
            assert abs(e3f(i) - f(i)) <= err
        print('Assign 03: Problem 01: Unit Test 01: pass')

    def test_assign_03_prob_01_ut_02(self):
        print('\n***** Assign 03: Problem 01: Unit Test 02 *****')
        e1 = make_prod(make_const(2.0), make_pwr('x', 3.0))
        e2 = make_prod(make_const(-5.0), make_pwr('x', 1.0))
        e3 = make_plus(e1, e2)
        e4 = make_plus(e3, make_const(0.0))
        e5 = make_prod(make_const(3.0), make_pwr('x', 1.0))
        e6 = make_plus(e5, make_const(1.0))
        e7 = make_prod(e4, e6)
        # print(e7)
        e7f = tof(deriv(e7))
        assert not e7f is None
        f = lambda x: 24*(x**3) +  6*(x**2) - 30*x - 5.0
        err = 0.0001
        for i in range(10):
            assert abs(e7f(i) - f(i)) <= err
        print('Assign 03: Problem 01: Unit Test 02: pass')

    def test_assign_03_prob_01_ut_03(self):
        print('\n***** Assign 03: Problem 01: Unit Test 03 *****')
        e1 = make_pwr('x', 2.0)
        e2 = make_plus(e1, make_prod(make_const(0.0),
                                     make_pwr('x', 1.0)))
        e3 = make_plus(e2, make_const(-1.0))
        e4 = make_pwr_expr(e3, 4.0)

        e5 = make_pwr('x', 2.0)
        e6 = make_plus(e5, make_prod(make_const(0.0),
                                     make_pwr('x', 1.0)))
        e7 = make_plus(e6, make_const(1.0))
        e8 = make_pwr_expr(e7, 5.0)
        
        e9 = make_prod(e4, e8)

        # print(e9)
        e9f = tof(deriv(e9))
        assert not e9f is None
        def drvf(x):
            return 2*x*((x**2 - 1.0)**3)*((x**2 + 1.0)**4)*(9*x**2 - 1.0)
        err = 0.0001
        for i in range(10):
            assert abs(e9f(i) - drvf(i)) <= err
        print('Assign 03: Problem 01: Unit Test 03: pass')

    def test_assign_03_prob_01_ut_04(self):
        print('\n***** Assign 03: Problem 01: Unit Test 04 *****')
        e1 = make_pwr('x', 2.0)
        e2 = make_plus(e1, make_prod(make_const(0.0),
                                     make_pwr('x', 1.0)))
        e3 = make_plus(e2, make_const(-1.0))
        e4 = make_pwr_expr(e3, 4.0)

        e5 = make_pwr('x', 2.0)
        e6 = make_plus(e5, make_prod(make_const(0.0),
                                     make_pwr('x', 1.0)))
        e7 = make_plus(e6, make_const(1.0))
        e8 = make_pwr_expr(e7, 5.0)
        
        e9 = make_prod(e4, e8)

        # print(e9)
        e9f = tof(deriv(e9))
        assert not e9f is None
        err = 0.000001
        def drvf(x):
            return 2*x*((x**2 - 1.0)**3)*((x**2 + 1.0)**4)*(9*x**2 - 1.0)
        for i in range(10):
            #print(e9f(i), drvf(i))
            assert abs(e9f(i) - drvf(i)) <= err
        print('Assign 03: Problem 01: Unit Test 04: pass')

    def test_assign_03_prob_01_ut_05(self):
        print('\n***** Assign 03: Problem 01: Unit Test 05 *****')
        e1 = make_plus(make_pwr('x', 1.0), make_const(1.0))
        
        e2 = make_pwr('x', 3.0)
        e3 = make_prod(make_const(0.0), make_pwr('x', 2.0))
        e4 = make_plus(e2, e3)
        e5 = make_prod(make_const(5.0), make_pwr('x', 1.0))
        e6 = make_plus(e4, e5)
        e7 = make_plus(e6, make_const(2.0))

        e8 = make_prod(e1, e7)
        # 1) print the expression we just constructed
        # print('-- function expression is:\n')
        # print(e8)
        # 2) differentiate and make sure that it not None
        drv = deriv(e8)
        assert not drv is None
        # print('\n-- derivative is:\n')
        # print(e8)
        # 3) convert drv into a function
        e8f = tof(drv)
        assert not e8f is None
        # steps 2) and 3) can be combined into tof(deriv(e6)).
        # 4) construct the ground truth function
        gt = lambda x: 4.0*(x**3) + 3*(x**2) + 10.0*x + 7.0
        # 5) compare the ground gruth with what we got in
        # step 3) on an appropriate number range.
        # print('\n--comparison with ground truth:\n')
        err = 0.00001
        for i in range(15):
            #print(e8f(i), gt(i))
            assert abs(e8f(i) - gt(i)) <= err
        print('Assign 03: Problem 01: Unit Test 05: pass')
    

    def test_assign_03_prob_01_ut_06(self):
        print('\n***** Assign 03: Problem 01: Unit Test 06 *****')
        e1 = make_prod(make_const(2.0), make_pwr('x', 4.0))
        e2 = make_prod(make_const(-1.0), make_pwr('x', 1.0))
        e3 = make_plus(e1, e2)
        e4 = make_plus(e3, make_const(1.0))
        
        e5 = make_prod(make_const(-1.0), make_pwr('x', 5.0))
        e6 = make_prod(make_const(0.0), make_pwr('x', 4.0))
        e7 = make_plus(e5, e6)
        e8 = make_prod(make_const(0.0), make_pwr('x', 3.0))
        e9 = make_plus(e7, e8)
        e10 = make_prod(make_const(0.0), make_pwr('x', 2.0))
        e11 = make_plus(e9, e10)
        e12 = make_prod(make_const(0.0), make_pwr('x', 1.0))
        e13 = make_plus(e11, e12)
        e14 = make_plus(e13, make_const(1.0))

        e15 = make_prod(e4, e14)
        # print('-- function expression is:\n')
        # print(e15)
        drv = deriv(e15)
        assert not drv is None
        # print('\n-- derivative is:\n')
        # print(drv)
        e15f = tof(drv)
        assert not e15f is None
        gt = lambda x: -18.0*(x**8) + 6.0*(x**5) - 5.0*(x**4) +  8.0*(x**3) - 1.0
        err = 0.00001
        # print('\n--comparison with ground truth:\n')
        for i in range(10):
            #print(e15f(i), gt(i)) 
            assert abs(e15f(i) - gt(i)) <= err
        print('Assign 03: Problem 01: Unit Test 06: pass')

    
    def test_assign_03_prob_01_ut_07(self):
        print('\n***** Assign 03: Problem 01: Unit Test 07 *****')
        q = make_quot(make_plus(make_pwr('x', 1.0), make_const(11.0)),
                      make_plus(make_pwr('x', 1.0), make_const(-3.0)))
        pex = make_pwr_expr(q, 3.0)
        # print('-- function expression is:\n')
        # print(pex)
        pexdrv = deriv(pex)
        assert not pexdrv is None
        # print('\n-- derivative is:\n')
        # print(pexdrv)
        pexdrvf = tof(pexdrv)
        assert not pexdrvf is None
        gt = lambda x: -42.0*(((x + 11.0)**2)/((x - 3.0)**4))
        err = 0.00001
        # print('\n--comparison with ground truth:\n')
        for i in range(100):
            if i != 3.0:
                #print(pexdrvf(i), gt(i))
                assert abs(pexdrvf(i) - gt(i)) <= err
        print('Assign 03: Problem 01: Unit Test 07: pass')

    def test_assign_03_prob_01_ut_08(self):
        print('\n***** Assign 03 Problem 01: Unit Test 08 *****')
        q = make_quot(make_plus(make_pwr('x', 1.0), make_const(11.0)),
                      make_plus(make_pwr('x', 1.0), make_const(-3.0)))
        pex = make_pwr_expr(q, 3.0)
        # print('-- function expression is:\n')
        # print(pex)
        pexdrv = deriv(pex)
        assert not pexdrv is None
        # print('\n-- derivative is:\n')
        # print(pexdrv)
        pexdrvf = tof(pexdrv)
        assert not pexdrvf is None
        gt = lambda x: -42.0*(((x + 11.0)**2)/((x - 3.0)**4))
        err = 0.00001
        # print('\n--comparison with ground truth:\n')
        for i in range(100):
            if i != 3.0:
                #print(pexdrvf(i), gt(i))
                assert abs(pexdrvf(i) - gt(i)) <= err
        print('Assign 03: Problem 01: Unit Test 08: pass')

    def test_assign_03_prob_01_ut_09(self):
        print('\n***** Assign 03: Problem 01: Unit Test 09 *****')
        n1 = make_plus(make_pwr('x', 2.0),
                       make_prod(make_const(0.0), make_pwr('x', 1.0)))
        n = make_plus(n1, make_const(-1.0))
        d1 = make_plus(make_pwr('x', 2.0),
                      make_prod(make_const(0.0), make_pwr('x', 1.0)))
        d = make_plus(d1, make_const(1.0))
        q = make_quot(n, d)
        qdrv = deriv(q)
        assert not qdrv is None
        # print(qdrv)
        qdrvf = tof(qdrv)
        assert not qdrvf is None
        def gt_drvf(x):
            return (4.0*x)/((x**2 + 1.0)**2)
        err = 0.0001
        for i in range(10):
            #print qdrvf(i), gt_drvf(i)
            assert abs(qdrvf(i) - gt_drvf(i)) <= err
        print('Assign 03: Problem 01: Unit Test 09: pass')

    def test_assign_03_prob_01_ut_10(self):
        print('\n***** Assign 03: Problem 01: Unit Test 10 *****')
        q = make_quot(make_plus(make_pwr('x', 1.0), make_const(11.0)),
                      make_plus(make_pwr('x', 1.0), make_const(-3.0)))
        pex = make_pwr_expr(q, 3.0)
        # print('-- function expression is:\n')
        # print(pex)
        pexdrv = deriv(pex)
        assert not pexdrv is None
        # print('\n-- derivative is:\n')
        # print(pexdrv)
        pexdrvf = tof(pexdrv)
        assert not pexdrvf is None
        gt = lambda x: -42.0*(((x + 11.0)**2)/((x - 3.0)**4))
        err = 0.00001
        # print('\n--comparison with ground truth:\n')
        for i in range(10):
            if i != 3.0:
                #print(pexdrvf(i), gt(i))
                assert abs(pexdrvf(i) - gt(i)) <= 0.001
        print('Assign 03: Problem 01: Unit Test 10: pass')

    
    ### ************* Problem 02 UTs *******************************

    def test_assign_03_prob_02_ut_01(self):
        print('\n***** Assign 03: Problem 02: Unit Test 01 *****')
        e1 = make_prod(make_const(1.0/12.0), make_pwr('x', 2.0))
        e2 = make_prod(make_const(-10.0), make_pwr('x', 1.0))
        sum1 = make_plus(e1, e2)
        dmndf_expr = make_plus(sum1, make_const(300.0))
        num_units, rev, price = \
                   maximize_revenue(dmndf_expr,
                                    constraint=lambda x: 0 <= x <= 60)
        # print('x = ', num_units.get_val())
        # print('rev = ', rev.get_val())
        # print('price = ', price.get_val())
        err = 0.000000000001
        assert abs(num_units.get_val() - 20.0) <= err
        assert abs(rev.get_val() - 2666.6666666666665) <= err
        assert abs(price.get_val() - 133.33333333333331) <= err
        print('Assign 03: Problem 02: Unit Test 01: pass')

    def test_assign_03_prob_02_ut_02(self):
        print('\n***** Assign 03: Problem 02: Unit Test 02 *****')
        e1 = make_prod(make_const(1.0/15.0), make_pwr('x', 2.0))
        e2 = make_prod(make_const(-9.5), make_pwr('x', 1.0))
        sum1 = make_plus(e1, e2)
        dmndf_expr = make_plus(sum1, make_const(250.0))
        num_units, rev, price = \
                   maximize_revenue(dmndf_expr,
                                    constraint=lambda x: 0 <= x <= 70)
        # print('x = ', num_units.get_val())
        # print('rev = ', rev.get_val())
        # print('price = ', price.get_val())
        err = 0.000000000001
        assert abs(num_units.get_val() - 15.778556148876199) <= err
        assert abs(rev.get_val() - 1841.3770500257765) <= err
        assert abs(price.get_val() - 116.70123886189205) <= err
        print('Assign 03: Problem 02: Unit Test 02: pass')

    def test_assign_03_prob_02_ut_03(self):
        print('\n***** Assign 03: Problem 02: Unit Test 03 *****')
        e1 = make_prod(make_const(1.0/11.0), make_pwr('x', 2.0))
        e2 = make_prod(make_const(-11.0), make_pwr('x', 1.0))
        sum1 = make_plus(e1, e2)
        dmndf_expr = make_plus(sum1, make_const(350.0))
        num_units, rev, price = \
                   maximize_revenue(dmndf_expr,
                                    constraint=lambda x: 0 <= x <= 70)
        # print('x = ', num_units.get_val())
        # print('rev = ', rev.get_val())
        # print('price = ', price.get_val())
        err = 0.000000000001
        assert abs(num_units.get_val() - 21.80107916810982) <= err
        assert abs(rev.get_val() - 3344.199278613588) <= err
        assert abs(price.get_val() - 153.39604305026398) <= err
        print('Assign 03: Problem 02: Unit Test 03: pass')

    def test_assign_03_prob_02_ut_04(self):
        print('\n***** Assign 03: Problem 02: Unit Test 04 *****')
        dmndf_expr = make_plus(make_prod(make_const(-0.5),
                                         make_pwr('x', 1.0)),
                               make_const(6.0))
        # print(dmndf_expr)
        num_units, rev, price = maximize_revenue(dmndf_expr,
                                                 constraint=lambda x: 0 <= x <= 10)
        err = 0.0001
        # print('x = ', num_units.get_val())

        assert abs(num_units.get_val() - 6.0) <= err
        assert abs(rev.get_val() - 18.0) <= err
        assert abs(price.get_val() - 3.0) <= err
        print('Assign 03: Problem 02: Unit Test 04: pass')

    def test_assign_03_prob_02_ut_05(self):
        print('\n***** Assign 03: Problem 02: Unit Test 05 *****')
        dmndf_expr = make_plus(make_prod(make_const(-1.0/200.0),
                                         make_pwr('x', 1.0)),
                               make_const(12.0))
        # print(dmndf_expr)
        num_units, rev, price = maximize_revenue(dmndf_expr,
                                                 constraint=lambda x: 0 <= x <= 1500)
        err = 0.0001
        assert abs(num_units.get_val() - 1200.0) <= err
        assert abs(rev.get_val() - 7200.0) <= err
        assert abs(price.get_val() - 6.0) <= err
        print('Assign 03: Problem 02: Unit Test 05: pass')

    ### ************* Problem 03 UTs *******************************

    def test_assign_03_prob_03_ut_01(self):
        print('\n***** Assign 03: Problem 03: Unit Test 01 *****')
        yt = make_prod(make_const(0.02*math.pi),
                       make_pwr('r', 2.0))
        # print(yt)
        dydt = dydt_given_x_dxdt(yt, make_const(150.0),
                                 make_const(20.0))
        assert not dydt is None
        assert isinstance(dydt, const)
        # print(dydt)
        err = 0.0001
        assert abs(dydt.get_val() - 376.991118431) <= err
        print('Assign 03: Problem 02: Unit Test 01: pass')

    def test_assign_03_prob_03_ut_02(self):
        print('\n***** Assign 03: Problem 03: Unit Test 02 *****')
        yt = make_prod(make_const(0.04*math.pi),
                       make_pwr('r', 2.0))
        # print(yt)
        dydt = dydt_given_x_dxdt(yt, make_const(120.0),
                                 make_const(25.0))
        assert not dydt is None
        assert isinstance(dydt, const)
        # print(dydt)
        err = 0.0001
        assert abs(dydt.get_val() - 753.982236862) <= err
        #assert abs(rev.get_val() - 7200.0) <= err
        #assert abs(price.get_val() - 6.0) <= err
        print('Assign 03: Problem 02: Unit Test 02: pass')

    def test_assign_03_prob_03_ut_03(self):
        print('\n***** Assign 03: Problem 03: Unit Test 03 *****')
        yt = make_prod(make_const(0.003*math.pi),
                       make_pwr('r', 2.0))
        # print(yt)
        dydt = dydt_given_x_dxdt(yt, make_const(175.0),
                                 make_const(30.0))
        assert not dydt is None
        assert isinstance(dydt, const)
        # print(dydt)
        err = 0.0001
        assert abs(dydt.get_val() - 98.9601685881) <= err
        print('Assign 03: Problem 03: Unit Test 03: pass')

    ### ************* Problem 04 UTs *******************************

    def test_assign_03_prob_04_ut_01(self):
        print('\n***** Assign 03: Problem 04: Unit Test 01 *****')
        yt = make_prod(make_const(0.003*math.pi),
                    make_pwr('r', 3.0))
        # print(yt)
        dydt = dydt_given_x_dxdt(yt, make_const(10.3),
                                 make_const(-1.75))
        assert not dydt is None
        assert isinstance(dydt, const)
        # print(dydt)
        err = 0.0001
        assert abs(dydt.get_val() + 5.24934214275) <= err
        print('Assign 03: Problem 04: Unit Test 01: pass')

    def test_assign_03_prob_04_ut_02(self):
        print('\n***** Assign 03: Problem 04: Unit Test 02 *****')
        yt = make_prod(make_const(0.05*math.pi),
                    make_pwr('r', 3.0))
        # print(yt)
        dydt = dydt_given_x_dxdt(yt, make_const(11.5),
                                 make_const(-2.75))
        assert not dydt is None
        assert isinstance(dydt, const)
        # print(dydt)
        err = 0.0001
        assert abs(dydt.get_val() + 171.38369673) <= err
        print('Assign 03: Problem 04: Unit Test 02: pass')

    def test_assign_03_prob_04_ut_03(self):
        print('\n***** Assign 03: Problem 04: Unit Test 03 *****')
        yt = make_prod(make_const(0.0075*math.pi),
                    make_pwr('r', 3.0))
        # print(yt)
        dydt = dydt_given_x_dxdt(yt, make_const(5.5),
                                 make_const(-1.25))
        assert not dydt is None
        assert isinstance(dydt, const)
        # print(dydt)
        err = 0.0001
        assert abs(dydt.get_val() + 2.67280812481) <= err
        print('Assign 03: Problem 04: Unit Test 03: pass')

    ##########################################################
    # def unit tests for assign 4
    ##########################################################

    def test_assign_04_prob_01_ut_01_0(self):
        print('\n***** Assign 04: Problem 01: Unit Test 01 *****')
        fex = make_e_expr(make_prod(make_const(5.0),
        make_pwr('x', 1.0)))
        # print(fex)
        drv = deriv(fex)
        assert not drv is None
        # print(drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 5.0*(math.e**(5.0*x))
        for i in range(10):
            # print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= 0.001
        print('Assign 04: Problem 01: Unit Test 01: pass')

    def test_assign_04_prob_01_ut_02_0(self):
        print('\n***** Assign 04: Problem 01: Unit Test 02 *****')
        fex = make_e_expr(make_plus(make_pwr('x', 2.0),
        make_const(-1.0)))
        # print(fex)
        drv = deriv(fex)
        assert not drv is None
        # print(drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 2*x*(math.e**(x**2 - 1.0))
        err = 0.0001
        for i in range(10):
            # print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= err
        print('Assign 04: Problem 01: Unit Test 02: pass')

    def test_assign_04_prob_01_ut_03_0(self):
        print('\n***** Assign 04: Problem 01: Unit Test 03 *****')
        fex1 = make_quot(make_const(-1.0), make_pwr('x', 1.0))
        fex2 = make_e_expr(make_plus(make_pwr('x', 1.0), fex1))
        # print(fex2)
        drv = deriv(fex2)
        assert not drv is None
        # print(drv)
        drvf = tof(drv)
        assert not drvf is None
        def gt_drvf(x):
            d = (x - 1.0/x)
            return (math.e**d)*(1.0 + 1.0/(x**2))
        err = 0.0001
        for i in range(1, 10):
            # print drvf(i), gt_drvf(i)
            assert abs(gt_drvf(i) - drvf(i)) <= err
        print('Assign 04: Problem 01: Unit Test 03: pass')

    def test_assign_04_prob_01_ut_04_0(self):
        print('\n***** Assign 04: Problem 01: Unit Test 04 *****')
        n = make_prod(make_const(3.0),
        make_e_expr(make_prod(make_const(2.0),
        make_pwr('x', 1.0))))
        d = make_plus(make_const(1.0), make_pwr('x', 2.0))
        fex = make_quot(n, d)
        # print(fex)
        drv = deriv(fex)
        assert not drv is None
        # print(drv)
        drvf = tof(drv)
        assert not drvf is None
        def gt_drvf(x):
            n = 6.0*(math.e**(2.0*x))*(x**2 - x + 1.0)
            d = (1 + x**2)**2
            return n/d
        for i in range(-10, 10):
            # print drvf(i), gt_drvf(i)
            assert abs(gt_drvf(i) - drvf(i)) <= 0.001
        print('Assign 04: Problem 01: Unit Test 04: pass')

    def test_assign_04_prob_01_ut_05_0(self):
        print('\n***** Assign 04: Problem 01: Unit Test 05 *****')
        fex = make_pwr_expr(make_ln(make_pwr('x', 1.0)), 5.0)
        # print(fex)
        drv = deriv(fex)
        assert not drv is None
        # print(drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: (5.0*(math.log(x, math.e)**4))/x
        err = 0.0001
        for i in range(1, 5):
            # print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= err
        print('Assign 04: Problem 01: Unit Test 05: pass')

    def test_assign_04_prob_01_ut_06_0(self):
        print('\n***** Assign 04: Problem 01: Unit Test 06 *****')
        fex = make_prod(make_pwr('x', 1.0),
        make_ln(make_pwr('x', 1.0)))
        # print(fex)
        drv = deriv(fex)
        assert not drv is None
        # print(drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 1.0 + math.log(x, math.e)
        err = 0.0001
        for i in range(1, 10):
            # print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= err
        print('Assign 04: Problem 01: Unit Test 06: pass')

    def test_assign_04_prob_01_ut_07_0(self):
        print('\n***** Assign 04: Problem 01: Unit Test 07 *****')
        fex0 = make_prod(make_pwr('x', 1.0),
        make_e_expr(make_pwr('x', 1.0)))
        fex = make_ln(fex0)
        # print(fex)
        drv = deriv(fex)
        assert not drv is None
        # print(drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: (x + 1.0)/x
        err = 0.0001
        for i in range(1, 10):
            # print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= err
        for i in range(-10, -1):
            # print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= 0.001
        print('Assign 04: Problem 01: Unit Test 07: pass')

    def test_assign_04_prob_01_ut_08_0(self):
        print('\n***** Assign 04: Problem 01: Unit Test 08 *****')
        fex = make_ln(make_absv(make_pwr('x', 1.0)))
        # print(fex)
        drv = deriv(fex)
        assert not drv is None
        # print(drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 1.0/x
        err = 0.0001
        for i in range(1, 10):
            # print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= err
        print('Assign 04: Problem 01: Unit Test 08: pass')

    def test_assign_04_prob_01_ut_09_0(self):
        print('\n***** Assign 04: Problem 02: Unit Test 09 *****')
        fex = make_prod(make_pwr('x', 1.0), make_prod(make_plus(make_pwr('x', 1.0), make_const(1.0)), make_plus(make_pwr('x', 1.0), make_const(2.0))))
        # print(fex)
        drv = logdiff(fex)
        assert not drv is None
        # print(drv)
        drvf = tof(drv)
        assert not drvf is None
        def gt_drvf(x):
            z = x*(x + 1.0)*(x + 2.0)
            z2 = (1.0/x + 1.0/(x + 1.0) + 1.0/(x + 2.0))
            return z * z2
        err = 0.0001
        for i in range(1, 10):
            # print(drvf(i), gt_drvf(i))
            assert abs(gt_drvf(i) - drvf(i)) <= err
        for i in range(-10, -1):
            if i == -1 or i == -2:
                continue
            # print(drvf(i), gt_drvf(i))
            assert abs(gt_drvf(i) - drvf(i)) <= err
        print('Assign 04: Problem 02: Unit Test 09: pass')

    def test_assign_04_prob_01_ut_10_0(self):
        print('\n***** Assign 04: Problem 02: Unit Test 10 *****')
        fex1 = make_plus(make_pwr('x', 2.0), make_const(1.0))
        fex2 = make_plus(make_pwr('x', 3.0), make_const(-3.0))
        fex3 = make_plus(make_prod(make_const(2.0),
        make_pwr('x', 1.0)),
        make_const(5.0))
        fex = make_prod(fex1, make_prod(fex2, fex3))
        # print(fex)
        drv = logdiff(fex)
        assert not drv is None
        # print(drv)
        drvf = tof(drv)
        assert not drvf is None
        def gt_drvf(x):
            z = (x**2 + 1.0)*(x**3 - 3.0)*(2*x + 5.0)
            z2 = ((2.0*x)/(x**2 + 1) + (3.0*(x**2))/(x**3 - 3.0) \
            + 2.0/(2*x + 5.0))
            return z * z2
        for i in range(1, 10):
            # print(drvf(i), gt_drvf(i))
            assert abs(gt_drvf(i) - drvf(i)) <= 0.001
        print('Assign 04: Problem 02: Unit Test 10: pass')

    def test_assign_04_prob_01_ut_11_0(self):
        print('\n***** Assign 04: Problem 02: Unit Test 11 *****')
        fex1 = make_pwr_expr(make_plus(make_pwr('x', 1.0),
        make_const(1.0)),
        4.0)
        fex2 = make_pwr_expr(make_plus(make_prod(make_const(4.0),
        make_pwr('x', 1.0)),
        make_const(-1.0)),
        2.0)
        fex = make_prod(fex1, fex2)
        # print(fex)
        drv = logdiff(fex)
        assert not drv is None
        # print(drv)
        drvf = tof(drv)
        def gt_drvf(x):
            z1 = ((x + 1.0)**4.0) * ((4*x - 1.0)**2.0)
            z2 = (4.0/(x + 1.0)) + ( 8.0/(4*x - 1.0))
            return z1 * z2
        for i in range(0, 20):
            # print(drvf(i), gt_drvf(i))
            assert abs(gt_drvf(i) - drvf(i)) <= 0.001
        print('Assign 04: Problem 02: Unit Test 11: pass')

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
