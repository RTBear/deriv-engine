#!/usr/bin/python

#############################################################
# module: hw03_unit_tests.py
# description: unit tests for CS 3430: S19: Assignment 03
# bugs to vladimir kulyukin via canvas
##############################################################

#uncomment the next line if you use Py2
#from __future__ import print_function
import unittest
import math
from prod import prod
from maker import make_const, make_pwr, make_const, make_plus
from maker import make_prod, make_quot
from maker import make_pwr_expr
from const import const
from plus import plus
from tof import tof
from deriv import deriv
from hw03 import maximize_revenue, dydt_given_x_dxdt

class Assign03UnitTests(unittest.TestCase):

    ### ************* Problem 01 UTs *******************************
    def test_assign_03_prob_01_ut_01(self):
        print('\n***** Assign 03: Problem 01: Unit Test 01 *****')
        e1 = make_pwr('x', 2.0)
        e2 = make_pwr('x', 3.0)
        e3 = make_prod(e1, e2)
        print(e3)
        drv = deriv(e3)
        assert not drv is None
        print(drv)
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
        print(e7)
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

        print(e9)
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

        print(e9)
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
        print('-- function expression is:\n')
        print(e8)
        # 2) differentiate and make sure that it not None
        drv = deriv(e8)
        assert not drv is None
        print('\n-- derivative is:\n')
        print(e8)
        # 3) convert drv into a function
        e8f = tof(drv)
        assert not e8f is None
        # steps 2) and 3) can be combined into tof(deriv(e6)).
        # 4) construct the ground truth function
        gt = lambda x: 4.0*(x**3) + 3*(x**2) + 10.0*x + 7.0
        # 5) compare the ground gruth with what we got in
        # step 3) on an appropriate number range.
        print('\n--comparison with ground truth:\n')
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
        print('-- function expression is:\n')
        print(e15)
        drv = deriv(e15)
        assert not drv is None
        print('\n-- derivative is:\n')
        print(drv)
        e15f = tof(drv)
        assert not e15f is None
        gt = lambda x: -18.0*(x**8) + 6.0*(x**5) - 5.0*(x**4) +  8.0*(x**3) - 1.0
        err = 0.00001
        print('\n--comparison with ground truth:\n')
        for i in range(10):
            #print(e15f(i), gt(i)) 
            assert abs(e15f(i) - gt(i)) <= err
        print('Assign 03: Problem 01: Unit Test 06: pass')

    
    def test_assign_03_prob_01_ut_07(self):
        print('\n***** Assign 03: Problem 01: Unit Test 07 *****')
        q = make_quot(make_plus(make_pwr('x', 1.0), make_const(11.0)),
                      make_plus(make_pwr('x', 1.0), make_const(-3.0)))
        pex = make_pwr_expr(q, 3.0)
        print('-- function expression is:\n')
        print(pex)
        pexdrv = deriv(pex)
        assert not pexdrv is None
        print('\n-- derivative is:\n')
        print(pexdrv)
        pexdrvf = tof(pexdrv)
        assert not pexdrvf is None
        gt = lambda x: -42.0*(((x + 11.0)**2)/((x - 3.0)**4))
        err = 0.00001
        print('\n--comparison with ground truth:\n')
        for i in range(100):
            if i != 3.0:
                #print(pexdrvf(i), gt(i))
                assert abs(pexdrvf(i) - gt(i)) <= err
        print('Assign 03: UT07: Problem 01: Unit Test 07: pass')

    def test_assign_03_prob_01_ut_08(self):
        print('\n***** Assign 03: UT08: Problem 01: Unit Test 08 *****')
        q = make_quot(make_plus(make_pwr('x', 1.0), make_const(11.0)),
                      make_plus(make_pwr('x', 1.0), make_const(-3.0)))
        pex = make_pwr_expr(q, 3.0)
        print('-- function expression is:\n')
        print(pex)
        pexdrv = deriv(pex)
        assert not pexdrv is None
        print('\n-- derivative is:\n')
        print(pexdrv)
        pexdrvf = tof(pexdrv)
        assert not pexdrvf is None
        gt = lambda x: -42.0*(((x + 11.0)**2)/((x - 3.0)**4))
        err = 0.00001
        print('\n--comparison with ground truth:\n')
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
        print(qdrv)
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
        print('-- function expression is:\n')
        print(pex)
        pexdrv = deriv(pex)
        assert not pexdrv is None
        print('\n-- derivative is:\n')
        print(pexdrv)
        pexdrvf = tof(pexdrv)
        assert not pexdrvf is None
        gt = lambda x: -42.0*(((x + 11.0)**2)/((x - 3.0)**4))
        err = 0.00001
        print('\n--comparison with ground truth:\n')
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
        print('x = ', num_units.get_val())
        print('rev = ', rev.get_val())
        print('price = ', price.get_val())
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
        print('x = ', num_units.get_val())
        print('rev = ', rev.get_val())
        print('price = ', price.get_val())
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
        print('x = ', num_units.get_val())
        print('rev = ', rev.get_val())
        print('price = ', price.get_val())
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
        print(dmndf_expr)
        num_units, rev, price = maximize_revenue(dmndf_expr,
                                                 constraint=lambda x: 0 <= x <= 10)
        err = 0.0001
        print('x = ', num_units.get_val())

        assert abs(num_units.get_val() - 6.0) <= err
        assert abs(rev.get_val() - 18.0) <= err
        assert abs(price.get_val() - 3.0) <= err
        print('Assign 03: Problem 02: Unit Test 04: pass')

    def test_assign_03_prob_02_ut_05(self):
        print('\n***** Assign 03: Problem 02: Unit Test 05 *****')
        dmndf_expr = make_plus(make_prod(make_const(-1.0/200.0),
                                         make_pwr('x', 1.0)),
                               make_const(12.0))
        print(dmndf_expr)
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
        print(yt)
        dydt = dydt_given_x_dxdt(yt, make_const(150.0),
                                 make_const(20.0))
        assert not dydt is None
        assert isinstance(dydt, const)
        print(dydt)
        err = 0.0001
        assert abs(dydt.get_val() - 376.991118431) <= err
        print('Assign 03: Problem 02: Unit Test 01: pass')

    def test_assign_03_prob_03_ut_02(self):
        print('\n***** Assign 03: Problem 03: Unit Test 02 *****')
        yt = make_prod(make_const(0.04*math.pi),
                       make_pwr('r', 2.0))
        print(yt)
        dydt = dydt_given_x_dxdt(yt, make_const(120.0),
                                 make_const(25.0))
        assert not dydt is None
        assert isinstance(dydt, const)
        print(dydt)
        err = 0.0001
        assert abs(dydt.get_val() - 753.982236862) <= err
        #assert abs(rev.get_val() - 7200.0) <= err
        #assert abs(price.get_val() - 6.0) <= err
        print('Assign 03: Problem 02: Unit Test 02: pass')

    def test_assign_03_prob_03_ut_03(self):
        print('\n***** Assign 03: Problem 03: Unit Test 03 *****')
        yt = make_prod(make_const(0.003*math.pi),
                       make_pwr('r', 2.0))
        print(yt)
        dydt = dydt_given_x_dxdt(yt, make_const(175.0),
                                 make_const(30.0))
        assert not dydt is None
        assert isinstance(dydt, const)
        print(dydt)
        err = 0.0001
        assert abs(dydt.get_val() - 98.9601685881) <= err
        print('Assign 03: Problem 03: Unit Test 03: pass')

    ### ************* Problem 04 UTs *******************************

    def test_assign_03_prob_04_ut_01(self):
        print('\n***** Assign 03: Problem 04: Unit Test 01 *****')
        yt = make_prod(make_const(0.003*math.pi),
                    make_pwr('r', 3.0))
        print(yt)
        dydt = dydt_given_x_dxdt(yt, make_const(10.3),
                                 make_const(-1.75))
        assert not dydt is None
        assert isinstance(dydt, const)
        print(dydt)
        err = 0.0001
        assert abs(dydt.get_val() + 5.24934214275) <= err
        print('Assign 03: Problem 04: Unit Test 01: pass')

    def test_assign_03_prob_04_ut_02(self):
        print('\n***** Assign 03: Problem 04: Unit Test 02 *****')
        yt = make_prod(make_const(0.05*math.pi),
                    make_pwr('r', 3.0))
        print(yt)
        dydt = dydt_given_x_dxdt(yt, make_const(11.5),
                                 make_const(-2.75))
        assert not dydt is None
        assert isinstance(dydt, const)
        print(dydt)
        err = 0.0001
        assert abs(dydt.get_val() + 171.38369673) <= err
        print('Assign 03: Problem 04: Unit Test 02: pass')

    def test_assign_03_prob_04_ut_03(self):
        print('\n***** Assign 03: Problem 04: Unit Test 03 *****')
        yt = make_prod(make_const(0.0075*math.pi),
                    make_pwr('r', 3.0))
        print(yt)
        dydt = dydt_given_x_dxdt(yt, make_const(5.5),
                                 make_const(-1.25))
        assert not dydt is None
        assert isinstance(dydt, const)
        print(dydt)
        err = 0.0001
        assert abs(dydt.get_val() + 2.67280812481) <= err
        print('Assign 03: Problem 04: Unit Test 03: pass')
    
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
