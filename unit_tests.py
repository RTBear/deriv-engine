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
from hw05 import expected_rev_dir,c14_carbon_dating,demand_elasticity,find_growth_model,is_demand_elastic,radioactive_decay,solve_pdeq,solve_pdeq_with_init_cond
from antideriv import antideriv
from riemann import riemann_approx, riemann_approx_with_gt, plot_riemann_error
from graphdrv import graph_drv
from graph import graph_funcs

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

    def test_assgn_01_ut_001(self):
        print('\n***** Assign 01: Unit Test 001 ************')
        prd = prod(mult1=make_const(2.0),
                   mult2=make_pwr('x', 5.0))
        # graph_drv(prd, [-3.0, 3.0], [-50, 50.0])
        print('Assign 01: Unit Test 01: pass')
    
    def test_assgn_01_ut_002(self):
        print('\n***** Assign 01: Unit Test 002 ************')
        fex1 = make_pwr('x', 4.0)
        fex2 = make_pwr('x', 3.0)
        fex3 = make_pwr('x', 1.0)
        fex4 = plus(elt1=fex1, elt2=fex2)
        fex5 = plus(elt1=fex4, elt2=fex3)
        # graph_drv(fex5, [-2.5, 2.5], [-10.0, 10.0])
        print('Assign 01: Unit Test 02: pass')

    def test_assgn_01_prob_02_ut_03(self):
        print('\n***** Assign 01: Unit Test 03 ************')
        fex1 = prod(mult1=make_const(-1.0),
                    mult2=make_pwr('x', 2.0))
        fex2 = plus(elt1=fex1, elt2=make_const(2.0))
        # graph_drv(fex2, [-10, 10], [-50.0, 25.0])
        print('Assign 01: Unit Test 03: pass')

    def test_assgn_01_prob_02_ut_04(self):
        print('\n***** Assign 01: Unit Test 04 ************')
        fex1 = prod(mult1=make_const(2),
                    mult2=make_pwr('x', 2.0))
        fex2 = plus(elt1=fex1, elt2=make_const(2.0))
        # graph_drv(fex2, [-10, 10], [-50.0, 50.0])
        print('Assign 01: Unit Test 04: pass')

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
        print(fex)
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

        ##########################################################
        ### DR K UNIT TESTS HW04 #################################
        ##########################################################
    def test_assign_04_prob_01_ut_01_01(self):
        print('\n***** HW4 Problem 01: UT 01 ************')
        fex = make_e_expr(make_prod(make_const(5.0),
                                    make_pwr('x', 1.0)))
        # print(fex)
        drv = deriv(fex)
        assert not drv is None
        # print(drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 5.0*(math.e**(5.0*x))
        err = 0.0001
        for i in range(10):
            #print(drvf(i), gt(i))
            # the numbers get pretty large pretty fast.
            assert abs(gt(i) - drvf(i)) <= err
        print('HW4 Problem 01: UT 01: pass')

    def test_assign_04_prob_01_ut_02(self):
        print('\n***** HW4 Problem 01: UT 02 ************')
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
            #print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= err
        print('HW4 Problem 01: UT 02: pass')

    def test_assign_04_prob_01_ut_03(self):
        print('\n***** HW4 Problem 01: UT 03 ************')
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
            #print drvf(i), gt_drvf(i)
            # the numbers are too large.
            assert abs(gt_drvf(i) - drvf(i)) <= err
        print('HW4 Problem 01: UT 03: pass')

    def test_assign_04_prob_01_ut_04(self):
        print('\n***** HW4 Problem 01: UT 04 ************')
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
            #print drvf(i), gt_drvf(i)
            # the numbers get pretty large.
            assert abs(gt_drvf(i) - drvf(i)) <= 0.001
        print('HW4 Problem 01: UT 04: pass')

    def test_assign_04_prob_01_ut_05(self):
        print('\n***** HW4 Problem 01: UT 05 ************')
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
        print('HW4 Problem 01: UT 05: pass')

    def test_assign_04_prob_01_ut_06(self):
        print('\n***** HW4 Problem 01: UT 06 ************')
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
        #     print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= err
        print('HW4 Problem 01: UT 06: pass')

    def test_assign_04_prob_01_ut_07(self):
        print('\n***** HW4 Problem 01: UT 07 ************')
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
            #print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= err
        for i in range(-10, -1):
            #print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= 0.001
        print('HW4 Problem 01: UT 07: pass')

    def test_assign_04_prob_01_ut_08(self):
        print('\n***** HW4 Problem 01: UT 08 ************')
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
            #print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= err
        print('HW4 Problem 01: UT 08: pass')

    def test_assign_04_prob_02_ut_01(self):
        print('\n***** HW4 Problem 02: UT 01 ************')
        fex = make_prod(make_pwr('x', 1.0),
                        make_prod(make_plus(make_pwr('x', 1.0),
                                            make_const(1.0)),
                                  make_plus(make_pwr('x', 1.0),
                                            make_const(2.0))))
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
            #print(drvf(i), gt_drvf(i))
            assert abs(gt_drvf(i) - drvf(i)) <= err
        for i in range(-10, -1):
            if i == -1 or i == -2:
                continue
            #print(drvf(i), gt_drvf(i))
            assert abs(gt_drvf(i) - drvf(i)) <= err
        print('HW4 Problem 02: UT 01: pass')

    def test_assign_04_prob_02_ut_02(self):
        print('\n***** HW4 Problem 02: UT 2 ************')
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
            #print(drvf(i), gt_drvf(i))
            assert abs(gt_drvf(i) - drvf(i)) <= 0.001
        print('HW4 Problem 02: UT 02: pass')

    def test_assign_04_prob_02_ut_03(self):
        print('\n***** HW4 Problem 02: UT 03 ************')
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
            #print(drvf(i), gt_drvf(i))
            assert abs(gt_drvf(i) - drvf(i)) <= 0.001
        print('HW4 Problem 02: UT 03: pass')
    
    def test_assign_05_prob_01_ut_1_0(self):
        print('\n***** Assign 05: Problem 01: Unit Test 1 *****')
        eq = solve_pdeq(make_const(1.0), make_const(1.0))
        assert not eq is None
        # print(eq)
        eqf = tof(eq)
        assert not eqf is None
        err = 0.0001
        gt = lambda t: math.e**t
        for t in range(100):
            assert abs(gt(t) - eqf(t)) <= err
        print('Assign 05: Problem 01: Unit Test 1: pass')

    def test_assign_05_prob_01_ut_2_0(self):
        print('\n***** Assign 05: Problem 01: Unit Test 2 *****')
        eq = solve_pdeq(make_const(4.0), make_const(1.0/3.0))
        assert not eq is None
        # print(eq)
        eqf = tof(eq)
        assert not eqf is None
        gt = lambda t: math.e**((1.0/12.0)*t)
        for t in range(100):
            assert abs(gt(t) - eqf(t)) <= 0.0001
        print('Assign 05: Problem 01: Unit Test 2: pass')

    def test_assign_05_prob_01_ut_3_0(self):
        print('\n***** Assign 05: Problem 01: Unit Test 3 *****')
        eq = solve_pdeq_with_init_cond(make_const(1.0),
        make_const(3.0))
        assert not eq is None
        # print(eq)
        eqf = tof(eq)
        assert not eqf is None
        def gt(t): return math.e**(3.0*t)
        err = 0.0001
        for t in range(100):
            assert abs(gt(t) - eqf(t)) <= err
        print('Assign 05: Problem 01: Unit Test 3: pass')

    def test_assign_05_prob_04_ut_1_0(self):
        print('\n***** Assign 05: Problem 04: Unit Test 1 *****')
        age = c14_carbon_dating(make_const(0.8))
        assert not age is None
        # print(age)
        gt = 1860
        err = 0.0001
        assert abs(gt - age.get_val()) <= err
        print('Assign 05: Problem 04: Unit Test 1: pass')

    def test_assign_05_prob_05_ut_1_0(self):
        print('\n***** Assign 05: Problem 05: Unit Test 1 *****')
        price = const(30.0)
        demand_eq = plus(const(100.0), prod(const(-2.0),make_pwr('x',1.0)))
        el = demand_elasticity(demand_eq, price)
        # print(is_demand_elastic(demand_eq, price))
        # print('exp dir +1')
        # print(expected_rev_dir(demand_eq, price, const(1)))
        # print('exp dir -1')
        # print(expected_rev_dir(demand_eq, price, const(-1)))

        assert not el is None
        # print(el)
        gt = 3.0/2.0
        err = 0.0001
        assert abs(gt - el.get_val()) <= err
        print('Assign 05: Problem 05: Unit Test 1: pass')

    ############################################################
    ####### GRADING UNIT TESTS FOR HW05 ########################
    ############################################################

    ### ************* HW05: Problem 01 UTs *******************************
    def test_assign_05_prob_01_ut_01(self):
        print('\n***** Assign 05: Problem 01: Unit Test 01 *****')
        eq = solve_pdeq(make_const(1.0), make_const(1.0))
        assert not eq is None
        # print(eq)
        eqf = tof(eq)
        assert not eqf is None
        err = 0.0001
        gt = lambda t: math.e**t
        for t in range(100):
            assert abs(gt(t) - eqf(t)) <= err 
        print('Assign 05: Problem 01: Unit Test 01: pass')

    def test_assign_05_prob_01_ut_02(self):
        print('\n***** Assign 05: Problem 01: Unit Test 02 *****')
        eq = solve_pdeq(make_const(1.0), make_const(1.7))
        assert not eq is None
        # print(eq)
        eqf = tof(eq)
        assert not eqf is None
        err = 0.0001
        gt = lambda t: math.e**(1.7*t)
        for t in range(100):
            assert abs(gt(t) - eqf(t)) <= err 
        print('Assign 05: Problem 01: Unit Test 02: pass')

    def test_assign_05_prob_01_ut_03(self):
        print('\n***** Assign 05: Problem 01: Unit Test 03 *****')
        eq = solve_pdeq(make_const(1.0), make_const(0.4))
        assert not eq is None
        # print(eq)
        eqf = tof(eq)
        assert not eqf is None
        err = 0.0001
        gt = lambda t: math.e**(0.4*t)
        for t in range(100):
            assert abs(gt(t) - eqf(t)) <= err 
        print('Assign 05: Problem 01: Unit Test 03: pass')

    def test_assign_05_prob_01_ut_04(self):
        print('\n***** Assign 05: Problem 01: Unit Test 04 *****')
        eq = solve_pdeq(make_const(2.0), make_const(0.5))
        assert not eq is None
        # print(eq)
        eqf = tof(eq)
        assert not eqf is None
        gt = lambda t: math.e**(0.25*t)
        for t in range(100):
            assert abs(gt(t) - eqf(t)) <= 0.0001 
        print('Assign 05: Problem 01: Unit Test 04: pass')

    def test_assign_05_prob_01_ut_05(self):
        print('\n***** Assign 05: Problem 01: Unit Test 05 *****')
        eq = solve_pdeq(make_const(4.0), make_const(1.0/3.0))
        assert not eq is None
        # print(eq)
        eqf = tof(eq)
        assert not eqf is None
        gt = lambda t: math.e**((1.0/12.0)*t)
        for t in range(100):
            assert abs(gt(t) - eqf(t)) <= 0.0001 
        print('Assign 05: Problem 01: Unit Test 05: pass')
    
    def test_assign_05_prob_01_ut_06(self):
        print('\n***** Assign 05: Problem 01: Unit Test 06 *****')
        eq = solve_pdeq_with_init_cond(make_const(1.0),
                                       make_const(3.0))
        assert not eq is None
        # print(eq)
        eqf = tof(eq)
        assert not eqf is None
        def gt(t): return math.e**(3.0*t)
        err = 0.0001
        for t in range(100):
            #print gt(t), eqf(t)
            assert abs(gt(t) - eqf(t)) <= err
        print('Assign 05: Problem 01: Unit Test 06: pass')

    def test_assign_05_prob_01_ut_07(self):
        print('\n***** Assign 05: Problem 01: Unit Test 07 *****')
        eq = solve_pdeq_with_init_cond(make_const(2.0),
                                       make_const(2.0))
        assert not eq is None
        # print(eq)
        eqf = tof(eq)
        assert not eqf is None
        def gt(t): return 2.0*math.e**(2.0*t)
        for t in range(100):
            #print gt(t), eqf(t)
            assert abs(gt(t) - eqf(t)) <= 0.0001
        print('Assign 05: Problem 01: Unit Test 07: pass')

    def test_assign_05_prob_01_ut_08(self):
        print('\n***** Assign 05: Problem 01: Unit Test 08 *****')
        eq = solve_pdeq_with_init_cond(make_const(5.0),
                                       make_const(0.6))
        assert not eq is None
        # print(eq)
        eqf = tof(eq)
        assert not eqf is None
        def gt(t): return 5.0*math.e**(0.6*t)
        for t in range(100):
            #print gt(t), eqf(t)
            assert abs(gt(t) - eqf(t)) <= 0.0001
        print('Assign 05: Problem 01: Unit Test 08: pass')

    def test_assign_05_prob_01_ut_09(self):
        print('\n***** Assign 05: Problem 01: Unit Test 09 *****')
        eq = solve_pdeq_with_init_cond(make_const(12.0),
                                       make_const(1/6.0))
        assert not eq is None
        # print(eq)
        eqf = tof(eq)
        assert not eqf is None
        def gt(t): return 12.0*math.e**((1.0/6)*t)
        for t in range(100):
            #print gt(t), eqf(t)
            assert abs(gt(t) - eqf(t)) <= 0.0001
        print('Assign 05: Problem 01: Unit Test 09: pass')

    def test_assign_05_prob_01_ut_10(self):
        print('\n***** Assign 05: Problem 01: Unit Test 10 *****')
        eq = solve_pdeq_with_init_cond(make_const(4.0),
                                       make_const(1.0))
        assert not eq is None
        # print(eq)
        eqf = tof(eq)
        assert not eqf is None
        def gt(t): return 4.0*math.e**t
        for t in range(100):
            #print gt(t), eqf(t)
            assert abs(gt(t) - eqf(t)) <= 0.0001
        print('Assign 05: Problem 01: Unit Test 10: pass')

    ### ************* HW05: Problem 02 UTs *******************************

    def test_assign_05_prob_02_ut_01(self):
        print('\n***** Assign 05: Problem 02: Unit Test 01 *****')
        eq = find_growth_model(make_const(20000.0),
                                  make_const(2.0),
                                  make_const(4.0))
        assert not eq is None
        # print(eq)
        eqf = tof(eq)
        assert not eqf is None
        def gt(t): return 20000.0*(math.e**((math.log(4.0, math.e)/2.0)*t))
        err = 0.0001
        #print(eqf(0.5))
        #print(gt(0.5))
        #assert abs(eqf(0.5) - gt(0.5)) <= err
        for t in range(100):
            #print gt(t), eqf(t)
            assert abs(gt(t) - eqf(t)) <= err 
        print('Assign 05: Problem 02: Unit Test 01: pass')
        print("PROBLEM: " + str(eqf(0.5)))
        #plot_bacteria_culture_growth(eqf, 0, 50)

    def test_assign_05_prob_02_ut_02(self):
        print('\n***** Assign 05: Problem 02: Unit Test 02 *****')
        eq = find_growth_model(make_const(10000.0),
                                  make_const(1.5),
                                  make_const(3.0))
        assert not eq is None
        # print(eq)
        eqf = tof(eq)
        assert not eqf is None
        def gt(t): return 10000.0*(math.e**((math.log(3.0, math.e)/1.5)*t))
        err = 0.0001
        #print(eqf(0.5))
        #print(gt(0.5))
        #assert abs(eqf(0.5) - gt(0.5)) <= err
        for t in range(100):
            #print gt(t), eqf(t)
            assert abs(gt(t) - eqf(t)) <= err 
        print('Assign 05: Problem 02: Unit Test 02: pass')
        #plot_bacteria_culture_growth(eqf, 0, 50)

    def test_assign_05_prob_02_ut_03(self):
        print('\n***** Assign 05: Problem 02: Unit Test 03 *****')
        eq = find_growth_model(make_const(50000.0),
                                  make_const(3.0),
                                  make_const(5.0))
        assert not eq is None
        # print(eq)
        eqf = tof(eq)
        assert not eqf is None
        def gt(t): return 50000.0*(math.e**((math.log(5.0, math.e)/3.0)*t))
        err = 0.0001
        #print(eqf(0.5))
        #print(gt(0.5))
        #assert abs(eqf(0.5) - gt(0.5)) <= err
        for t in range(100):
            #print gt(t), eqf(t)
            assert abs(gt(t) - eqf(t)) <= err 
        print('Assign 05: Problem 02: Unit Test 03: pass')
        #plot_bacteria_culture_growth(eqf, 0, 50)

    ### ************* HW05: Problem 03 UTs *******************************

    def test_assign_05_prob_03_ut_01(self):
        print('\n***** Assign 05: Problem 03: Unit Test 01 *****')
        #eq, eqf, amount = radioactive_decay(make_const(-0.021),
        #                                  make_const(8.0),
        #                                   make_const(10.0))
        eq = radioactive_decay(make_const(-0.021),
                               make_const(8.0),
                               make_const(10.0))
        assert not eq is None
        # print(eq)
        #print(amount)
        eqf = tof(eq)
        assert not eqf is None
        def gt(t): return 8.0*(math.e**(-0.021*t))
        err = 0.0001
        #print(eqf(0.5))
        #print(gt(0.5))
        #assert abs(eqf(0.5) - gt(0.5)) <= err
        for t in range(100):
            #print gt(t), eqf(t)
            assert abs(gt(t) - eqf(t)) <= err 
        print('Assign 05: Problem 03: Unit Test 01: pass')
        #self.plot_bacteria_culture_growth(eqf)
        #plot_radioactive_decay(eqf, 0,300)

    def test_assign_05_prob_03_ut_02(self):
        print('\n***** Assign 05: Problem 03: Unit Test 02 *****')
        #eq, eqf, amount = radioactive_decay(make_const(-0.041),
        #                                   make_const(8.0),
        #                                   make_const(10.0))
        eq = radioactive_decay(make_const(-0.041),
                               make_const(8.0),
                               make_const(10.0))
        assert not eq is None
        # print(eq)
        #print(amount)
        eqf = tof(eq)
        assert not eqf is None
        def gt(t): return 8.0*(math.e**(-0.041*t))
        err = 0.0001
        #print(eqf(0.5))
        #print(gt(0.5))
        #assert abs(eqf(0.5) - gt(0.5)) <= err
        for t in range(100):
            #print gt(t), eqf(t)
            assert abs(gt(t) - eqf(t)) <= err 
        print('Assign 05: Problem 03: Unit Test 02: pass')
        #self.plot_bacteria_culture_growth(eqf)
        #plot_radioactive_decay(eqf, 0,300)

    def test_assign_05_prob_03_ut_03(self):
        print('\n***** Assign 05: Problem 03: Unit Test 03 *****')
        #eq, eqf, amount = radioactive_decay(make_const(-0.0032),
        #                                   make_const(8.0),
        #                                   make_const(10.0))
        eq = radioactive_decay(make_const(-0.0032),
                               make_const(8.0),
                               make_const(10.0))
        assert not eq is None
        # print(eq)
        #print(amount)
        eqf = tof(eq)
        assert not eqf is None
        def gt(t): return 8.0*(math.e**(-0.0032*t))
        err = 0.0001
        #print(eqf(0.5))
        #print(gt(0.5))
        #assert abs(eqf(0.5) - gt(0.5)) <= err
        for t in range(100):
            #print gt(t), eqf(t)
            assert abs(gt(t) - eqf(t)) <= err 
        print('Assign 05: Problem 03: Unit Test 03: pass')
        #self.plot_bacteria_culture_growth(eqf)
        #plot_radioactive_decay(eqf, 0, 300)

    ### ************* HW05: Problem 04 UTs *******************************

    # to solve
    def test_assign_05_prob_04_ut_01(self):
        print('\n***** Assign 05: Problem 04: Unit Test 01 *****')
        age = c14_carbon_dating(make_const(0.2))
        # print(age)
        assert abs(age.get_val() - 13412.0) <= 0.00001
        print('Assign 05: Problem 04: Unit Test 01: pass')

    # to solve
    def test_assign_05_prob_04_ut_02(self):
        print('\n***** Assign 05: Problem 04: Unit Test 02 *****')
        age = c14_carbon_dating(make_const(0.583))
        # print(age)
        assert abs(age.get_val() - 4497.0) <= 0.00001
        print('Assign 05: Problem 04: Unit Test 02: pass')

    # give as a unit test
    def test_assign_05_prob_04_ut_03(self):
        print('\n***** Assign 05: Problem 04: Unit Test 03 *****')
        age = c14_carbon_dating(make_const(0.80))
        # print(age)
        assert abs(age.get_val() - 1860.0) <= 0.00001
        print('Assign 05: Problem 04: Unit Test 03: pass')

    ### ************* HW05: Problem 05 UTs *******************************

    def test_assign_05_prob_05_ut_01(self):
        print('\n***** Assign 05: Problem 05: Unit Test 01 *****')
        fex0 = make_quot(make_const(18000.0), make_pwr('p', 1.0))
        deq = make_plus(fex0, make_const(-1500.0))
        ## change these to assertions later
        print(demand_elasticity(deq, make_const(6.0)))
        print(is_demand_elastic(deq, make_const(6.0)))
        print(expected_rev_dir(deq, make_const(6.0), make_const(-1.0)))
        print('Assign 05: Problem 05: Unit Test 01: pass')

    def test_assign_05_prob_05_ut_02(self):
        print('\n***** Assign 05: Problem 05: Unit Test 02 *****')
        demand_eq = make_plus(make_const(100.0),
                              make_prod(make_const(-2.0),
                                        make_pwr('p', 1.0)))
        print(demand_elasticity(demand_eq, make_const(30.0)))
        print(demand_elasticity(demand_eq, make_const(20.0)))
        print(is_demand_elastic(demand_eq, make_const(30.0)))
        print(is_demand_elastic(demand_eq, make_const(20.0)))
        print(expected_rev_dir(demand_eq, make_const(30.0), make_const(-1.0)))
        print(expected_rev_dir(demand_eq, make_const(30.0), make_const(+1.0)))
        print(expected_rev_dir(demand_eq, make_const(20.0), make_const(-1.0)))
        print(expected_rev_dir(demand_eq, make_const(20.0), make_const(+1.0)))
        print('Assign 05: Problem 05: Unit Test 02: pass')

    def test_assign_07_prob_01_ut_01_0(self):
        print('\n***** Assign 07: Problem 01: Unit Test 01 *****')
        fex = make_pwr('x', 2.0)
        # print(fex)
        afex = antideriv(fex)
        assert not afex is None
        def gt(x): return (1.0/3.0)*(x**3.0)
        afexf = tof(afex)
        assert not afexf is None
        err = 0.0001
        for i in range(1, 101):
            assert abs(afexf(i) - gt(i)) <= err
            # print(afex)
        print('Assign 07: Problem 01: Unit Test 01: pass')

    def test_assign_07_prob_01_ut_02_0(self):
        print('\n***** Assign 07: Problem 01: Unit Test 02 *****')
        fex = make_e_expr(make_prod(make_const(-2.0),
        make_pwr('x', 1.0)))
        # print(fex)
        afex = antideriv(fex)
        assert not afex is None
        # print(afex)
        def gt(x): return (-0.5)*(math.e**(-2.0*x))
        afexf = tof(afex)
        assert not afexf is None
        err = 0.0001
        for i in range(0, 101):
            assert abs(afexf(i) - gt(i)) <= err
            # print(afex)
        print('Assign 07: Problem 01: Unit Test 02: pass')

    def test_assign_07_prob_01_ut_03_0(self):
        print('\n***** Assign 07: Problem 01: Unit Test 03 *****')
        fex = make_pwr('x', 0.5)
        # print(fex)
        afex = antideriv(fex)
        assert not afex is None
        def gt(x): return (2.0/3.0)*(x**(3.0/2.0))
        afexf = tof(afex)
        assert not afexf is None
        err = 0.0001
        for i in range(1, 101):
            assert abs(afexf(i) - gt(i)) <= err
            # print(afex)
        print('Assign 07: Problem 01: Unit Test 03: pass')

    def test_assign_07_prob_01_ut_04_0(self):
        print('\n***** Assign 07: Problem 01: Unit Test 04 *****')
        fex = make_pwr('x', -2.0)
        # print(fex)
        afex = antideriv(fex)
        assert not afex is None
        def gt(x): return -1.0/x
        afexf = tof(afex)
        assert not afexf is None
        err = 0.0001
        for i in range(1, 101):
            assert abs(afexf(i) - gt(i)) <= err
            # print(afex)
        print('Assign 07: Problem 01: Unit Test 04: pass')

    def test_assign_07_prob_01_ut_05_0(self):
        print('\n***** Assign 07: Problem 01: Unit Test 05 *****')
        fex = make_pwr('x', -1.0)
        # print(fex)
        afex = antideriv(fex)
        assert not afex is None
        # print(afex)
        afexf = tof(afex)
        assert not afexf is None
        def gt(x): return math.log(abs(x), math.e)
        err = 0.0001
        for i in range(1, 101):
            assert abs(afexf(i) - gt(i)) <= err
        for i in range(-100, 0):
            # print(afexf(i),gt(i))
            assert abs(afexf(i) - gt(i)) <= err
        print('Assign 07: Problem 01: Unit Test 05: pass')

    def test_assign_07_prob_01_ut_06_0(self):
        print('\n***** Assign 07: Problem 01: Unit Test 06 *****')
        fex1 = make_pwr('x', -3.0)
        fex2 = make_prod(make_const(7.0),
                         make_e_expr(make_prod(make_const(5.0),
                                               make_pwr('x', 1.0))))
        fex3 = make_prod(make_const(4.0),
                         make_pwr('x', -1.0))
        fex4 = make_plus(fex1, fex2)
        fex = make_plus(fex4, fex3)
        # print(fex)
        afex = antideriv(fex)
        assert not afex is None
        # print(afex)
        def gt(x):
            v1 = -0.5*(x**(-2.0))
            v2 = (7.0/5.0)*(math.e**(5.0*x))
            v3 = 4.0*(math.log(abs(x), math.e))
            return v1 + v2 + v3
        afexf = tof(afex)
        assert not afexf is None
        err = 0.002
        for i in range(1, 7):
            # print(i,afexf(i), gt(i),abs(afexf(i) - gt(i)))
            assert abs(afexf(i) - gt(i)) <= err
        print('Assign 07: Problem 01: Unit Test 06: pass')

    def test_assign_07_prob_01_ut_07_0(self):
        print('\n***** Assign 07: Problem 01: Unit Test 07 *****')
        fex = make_prod(make_const(4.0), make_pwr('x', 3.0))
        # print(fex)
        afex = antideriv(fex)
        assert not afex is None
        # print(afex)
        fexf = tof(fex)
        assert not fexf is None
        fex2 = deriv(afex)
        assert not fex2 is None
        # print(fex2)
        fex2f = tof(fex2)
        assert not fex2f is None
        err = 0.0001
        for i in range(11):
            assert abs(fexf(i) - fex2f(i)) <= err
        print('Assign 07: Problem 01: Unit Test 07: pass')

    def test_assign_07_prob_01_ut_08_0(self):
        print('\n***** Assign 07: Problem 01: Unit Test 08 *****')
        fex1 = make_plus(make_prod(make_const(5.0),
                                    make_pwr('x', 1.0)),
                        make_const(-7.0))
        fex = make_pwr_expr(fex1, -2.0)
        # print(fex)
        afex = antideriv(fex)
        assert not afex is None
        # print(afex)
        afexf = tof(afex)
        err = 0.0001
        def gt(x):
            return (-1.0/5.0)*((5*x - 7.0)**-1)
        for i in range(1, 100):
            # print(afexf(i) , gt(i))
            assert abs(afexf(i) - gt(i)) <= err
        fexf = tof(fex)
        assert not fexf is None
        fex2 = deriv(afex)
        assert not fex2 is None
        # print(fex2)
        fex2f = tof(fex2)
        assert not fex2f is None
        for i in range(1, 100):
            # print(fexf(i) , fex2f(i))
            assert abs(fexf(i) - fex2f(i)) <= err
        print('Assign 07: Problem 01: Unit Test 08: pass')
    
    def test_assign_07_prob_01_ut_09_0(self):
        print('\n***** Assign 07: Problem 01: Unit Test 09 *****')
        fex0 = make_plus(make_pwr('x', 1.0), make_const(2.0))
        fex1 = make_pwr_expr(fex0, -1.0)
        fex = make_prod(make_const(3.0), fex1)
        # print(fex)
        afex = antideriv(fex)
        # print(afex)
        err = 0.0001
        afexf = tof(afex)
        def gt(x):
            return 3.0*math.log(abs(2.0 + x), math.e)
        for i in range(1, 101):
            assert abs(afexf(i) - gt(i)) <= err
        assert not afex is None
        # print(afex)
        fexf = tof(fex)
        assert not fexf is None
        fex2 = deriv(afex)
        assert not fex2 is None
        # print(fex2)
        fex2f = tof(fex2)
        assert not fex2f is None
        for i in range(1, 1000):
            assert abs(fexf(i) - fex2f(i)) <= err
        print('Assign 07: Problem 01: Unit Test 09: pass')

    def test_assign_07_prob_01_ut_10_0(self):
        print('\n***** Assign 07: Problem 01: Unit Test 10 *****')
        fex0 = make_prod(make_const(3.0), make_pwr('x', 1.0))
        fex1 = make_plus(fex0, make_const(2.0))
        fex = make_pwr_expr(fex1, 4.0)
        # print(fex)
        afex = antideriv(fex)
        assert not afex is None
        # print(afex)
        afexf = tof(afex)
        err = 0.0001
        def gt(x):
            return (1.0/15)*((3*x + 2.0)**5)
        for i in range(1, 10):
            # print(afexf(i) , gt(i))
            assert abs(afexf(i) - gt(i)) <= err
        fexf = tof(fex)
        assert not fexf is None
        fex2 = deriv(afex)
        assert not fex2 is None
        # print(fex2)
        fex2f = tof(fex2)
        assert not fex2f is None
        # for i in range(1, 1000):
        print('Assign 07: Problem 01: Unit Test 10: pass')

    def test_assign_08_prob_01_ut_01_0(self):
        print('\n***** Assign 08: Problem 01: Unit Test 01 *****')
        fex = make_prod(make_const(3.0), make_pwr('x', 2.0))
        fex = make_plus(fex, make_e_expr(make_pwr('x', 1.0)))
        print(fex)
        print("LEFT")
        err_list = riemann_approx_with_gt(fex,
        make_const(-1.0),
        make_const(1.0),
        make_const(4.35),
        make_const(10),
        pp=-1)
        # for n, err in err_list:
        #     print(n, err)
        print('Assign 08: Problem 01: Unit Test 01: pass')

    def test_assign_08_prob_01_ut_02_0(self):
        print('\n***** Assign 08: Problem 01: Unit Test 02 *****')
        fex = make_prod(make_const(3.0), make_pwr('x', 2.0))
        fex = make_plus(fex, make_e_expr(make_pwr('x', 1.0)))
        print(fex)
        print("CENTER")

        err_list = riemann_approx_with_gt(fex,
                                        make_const(-1.0),
                                        make_const(1.0), 
                                        make_const(4.35), 
                                        make_const(10), 
                                        pp=0)

        # for n, err in err_list:
        #     print(n, err)
        print('Assign 08: Problem 01: Unit Test 02: pass')

    def test_assign_08_prob_01_ut_03_0(self):
        print('\n***** Assign 08: Problem 01: Unit Test 03 *****')
        fex = make_prod(make_const(3.0), make_pwr('x', 2.0))
        fex = make_plus(fex, make_e_expr(make_pwr('x', 1.0)))
        print(fex)
        print("RIGHT")

        err_list = riemann_approx_with_gt(fex, make_const(-1.0),
                                            make_const(1.0),
                                            make_const(4.35),
                                            make_const(10),
                                            pp=+1)
        # for n, err in err_list:
        #     print(n, err)
        print('Assign 08: Problem 01: Unit Test 03: pass')

    def test_assign_08_prob_01_ut_04_0(self):
        print('\n***** Assign 08: Problem 01: Unit Test 04 *****')
        fex = make_ln(make_pwr('x', 1.0))
        print(fex)
        err = 0.0001
        approx = riemann_approx(fex,
                                make_const(1.0),
                                make_const(2.0),
                                make_const(100),
                                pp=0)
        assert abs(approx.get_val() - 0.386296444432) <= err
        print('Assign 08: Problem 01: Unit Test 04: pass')

    def test_assign_08_prob_01_ut_04_1(self):
        print('\n***** Assign 08: Problem 01: Unit Test 04.1 *****')
        fex1 = prod(mult1=make_const(2),
                    mult2=make_pwr('x', 2.0))
        fex2 = plus(elt1=fex1, elt2=make_const(2.0))
        funcs = [fex2,deriv(fex2)]
        # graph_drv(fex2, [-10, 10], [-50.0, 50.0])
        # graph_funcs(funcs, [-10, 10], [-50.0, 50.0])
        print('Assign 08: Problem 01: Unit Test 04.1: pass')

    def test_assign_08_prob_01_ut_04_2(self):
        print('\n***** Assign 08: Problem 01: Unit Test 04.2 *****')
        fex = make_prod(make_const(3.0), make_pwr('x', 2.0))
        fex = make_plus(fex, make_e_expr(make_pwr('x', 1.0)))
        # plot_riemann_error(fex, make_const(-1.0),
        # make_const(1.0),
        # make_const(4.35),
        # make_const(100))
        print('Assign 08: Problem 01: Unit Test 04.2: pass')

    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
