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
from maker import make_const, make_pwr, make_prod, make_plus, make_point2d, make_quot, make_pwr_expr
from plus import plus
from tof import tof
from const import const
from deriv import deriv
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
        print(prd)
        print(drv)
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

    def test_assgn_03_prob_01_ut_01(self):
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

    def test_assgn_03_prob_01_ut_02(self):
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

    def test_assgn_03_prob_01_ut_03(self):
        print('\n***** Assign 03: Unit Test 03 ************')
        q = make_quot(make_plus(make_pwr('x', 1.0),
        make_const(11.0)),
        make_plus(make_pwr('x', 1.0), make_const(-3.0)))
        pex = make_pwr_expr(q, 3.0)
        # print('-- function expression is:\n')
        print(pex)
        pexdrv = deriv(pex)
        assert not pexdrv is None
        # print('\n-- derivative is:\n')
        print(pexdrv)
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

    def test_assgn_03_prob_02_ut_01(self):
        print('\n***** Assign 03: Unit Test 04 ************')
        e1 = make_prod(make_const(1.0/12.0), make_pwr('x', 2.0))
        e2 = make_prod(make_const(-10.0), make_pwr('x', 1.0))
        sum1 = make_plus(e1, e2)
        sum2 = plus(sum1,make_const(300.0))
        # drv = deriv(sum2)
        # print sum2
        # print drv
        xtrm = loc_xtrm_2nd_drv_test(sum2)
        for val in xtrm:
            print(val[0])
            print(val[1])
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

    def test_assgn_03_prob_03_ut_01(self):
        print('\n***** Assign 03: Unit Test 05 ************')
        yt = make_prod(make_const(0.02*math.pi), make_pwr('r', 2.0))
        # print(yt)
        dydt = dydt_given_x_dxdt(yt, make_const(150.0),make_const(20.0))
        assert not dydt is None
        assert isinstance(dydt, const)
        assert abs(dydt.get_val() - 376.991118431) < .001
        print('Assign 03: Unit Test 05: pass')

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
