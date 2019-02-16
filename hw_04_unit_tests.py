#!/usr/bin/python

###########################################
# module: hw04_unit_tests.py
# description: examples of unit tests and
# how to run them.
# bugs to vladimir kulyukin via canvas
###########################################

import unittest
import math
from maker import make_prod, make_const, make_pwr, make_e_expr
from maker import make_plus, make_quot, make_pwr_expr, make_ln
from maker import make_absv
from tof import tof
from deriv import deriv
from deriv import logdiff

class Assign04UnitTests(unittest.TestCase):

    def test_prob_01_ut_01(self):
        print('\n***** Problem 01: UT 01 ************')
        fex = make_e_expr(make_prod(make_const(5.0),
                                    make_pwr('x', 1.0)))
        print(fex)
        drv = deriv(fex)
        assert not drv is None
        print(drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 5.0*(math.e**(5.0*x))
        err = 0.0001
        for i in range(10):
            #print(drvf(i), gt(i))
            # the numbers get pretty large pretty fast.
            assert abs(gt(i) - drvf(i)) <= err
        print('Problem 01: UT 01: pass')

    def test_prob_01_ut_02(self):
        print('\n***** Problem 01: UT 02 ************')
        fex = make_e_expr(make_plus(make_pwr('x', 2.0),
                                    make_const(-1.0)))
        print(fex)
        drv = deriv(fex)
        assert not drv is None
        print(drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 2*x*(math.e**(x**2 - 1.0))
        err = 0.0001
        for i in range(10):
            #print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= err
        print('Problem 01: UT 02: pass')

    def test_prob_01_ut_03(self):
        print('\n***** Problem 01: UT 03 ************')
        fex1 = make_quot(make_const(-1.0), make_pwr('x', 1.0))
        fex2 = make_e_expr(make_plus(make_pwr('x', 1.0), fex1))
        print(fex2)
        drv = deriv(fex2)
        assert not drv is None
        print(drv)
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
        print('Problem 01: UT 03: pass')

    def test_prob_01_ut_04(self):
        print('\n***** Problem 01: UT 04 ************')
        n = make_prod(make_const(3.0),
                      make_e_expr(make_prod(make_const(2.0),
                                            make_pwr('x', 1.0))))                               
        d = make_plus(make_const(1.0), make_pwr('x', 2.0))
        fex = make_quot(n, d)
        print(fex)
        drv = deriv(fex)
        assert not drv is None
        print(drv)
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
        print('Problem 01: UT 04: pass')

    def test_prob_01_ut_05(self):
        print('\n***** Problem 01: UT 05 ************')
        fex = make_pwr_expr(make_ln(make_pwr('x', 1.0)), 5.0)
        print(fex)
        drv = deriv(fex)
        assert not drv is None
        print(drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: (5.0*(math.log(x, math.e)**4))/x
        err = 0.0001
        for i in range(1, 5):
            print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= err
        print('Problem 01: UT 05: pass')

    def test_prob_01_ut_06(self):
        print('\n***** Problem 01: UT 06 ************')
        fex = make_prod(make_pwr('x', 1.0),
                        make_ln(make_pwr('x', 1.0)))
        print(fex)
        drv = deriv(fex)
        assert not drv is None
        print(drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 1.0 + math.log(x, math.e)
        err = 0.0001
        for i in range(1, 10):
            print(drvf(i), gt(i))
        assert abs(gt(i) - drvf(i)) <= err
        print('Problem 01: UT 06: pass')

    def test_prob_01_ut_07(self):
        print('\n***** Problem 01: UT 07 ************')
        fex0 = make_prod(make_pwr('x', 1.0),
                         make_e_expr(make_pwr('x', 1.0)))
        fex = make_ln(fex0)
        print(fex)
        drv = deriv(fex)
        assert not drv is None
        print(drv)
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
        print('Problem 01: UT 07: pass')

    def test_prob_01_ut_08(self):
        print('\n***** Problem 01: UT 08 ************')
        fex = make_ln(make_absv(make_pwr('x', 1.0)))
        print(fex)
        drv = deriv(fex)
        assert not drv is None
        print(drv)
        drvf = tof(drv)
        assert not drvf is None
        gt = lambda x: 1.0/x
        err = 0.0001
        for i in range(1, 10):
            #print(drvf(i), gt(i))
            assert abs(gt(i) - drvf(i)) <= err
        print('Problem 01: UT 08: pass')

    def test_prob_02_ut_01(self):
        print('\n***** Problem 02: UT 01 ************')
        fex = make_prod(make_pwr('x', 1.0),
                        make_prod(make_plus(make_pwr('x', 1.0),
                                            make_const(1.0)),
                                  make_plus(make_pwr('x', 1.0),
                                            make_const(2.0))))
        drv = logdiff(fex)
        assert not drv is None
        print(drv)
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
        print('Problem 02: UT 01: pass')

    def test_prob_02_ut_02(self):
        print('\n***** Problem 02: UT 2 ************')
        fex1 = make_plus(make_pwr('x', 2.0), make_const(1.0))
        fex2 = make_plus(make_pwr('x', 3.0), make_const(-3.0))
        fex3 = make_plus(make_prod(make_const(2.0),
                                   make_pwr('x', 1.0)),
                         make_const(5.0))
        fex = make_prod(fex1, make_prod(fex2, fex3))
        print(fex)
        drv = logdiff(fex)
        assert not drv is None
        print(drv)
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
        print('Problem 02: UT 02: pass')

    def test_prob_02_ut_03(self):
        print('\n***** Problem 02: UT 03 ************')
        fex1 = make_pwr_expr(make_plus(make_pwr('x', 1.0),
                                       make_const(1.0)),
                             4.0)
        fex2 = make_pwr_expr(make_plus(make_prod(make_const(4.0),
                                                 make_pwr('x', 1.0)),
                                       make_const(-1.0)),
                             2.0)
        fex = make_prod(fex1, fex2)
        print(fex)
        drv = logdiff(fex)
        assert not drv is None
        print(drv)
        drvf = tof(drv)
        def gt_drvf(x):
            z1 = ((x + 1.0)**4.0) * ((4*x - 1.0)**2.0)
            z2 = (4.0/(x + 1.0)) + ( 8.0/(4*x - 1.0))
            return z1 * z2
        for i in range(0, 20):
            #print(drvf(i), gt_drvf(i))
            assert abs(gt_drvf(i) - drvf(i)) <= 0.001
        print('Problem 02: UT 03: pass')
    
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
