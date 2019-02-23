#!/usr/bin/python

#############################################################
# module: hw05_unit_tests.py
# description: unit tests for CS 3430: S19: Assignment 05
# bugs to vladimir kulyukin via canvas
##############################################################

#uncomment the next line if you use Py2
#from __future__ import print_function
import unittest
import math
from maker import make_const, make_quot, make_pwr, make_plus, make_prod
from tof import tof
from hw05 import solve_pdeq, solve_pdeq_with_init_cond, radioactive_decay
from hw05 import find_growth_model
# from hw05 import plot_bacteria_culture_growth
# from hw05 import plot_radioactive_decay
from hw05 import c14_carbon_dating
from hw05 import demand_elasticity, is_demand_elastic, expected_rev_dir
import numpy as np
import matplotlib.pyplot as plt

class Assign05UnitTests(unittest.TestCase):

    ### ************* HW05: Problem 01 UTs *******************************
    def test_assign_05_prob_01_ut_01(self):
        print('\n***** Assign 05: Problem 01: Unit Test 01 *****')
        eq = solve_pdeq(make_const(1.0), make_const(1.0))
        assert not eq is None
        print(eq)
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
        print(eq)
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
        print(eq)
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
        print(eq)
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
        print(eq)
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
        print(eq)
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
        print eq
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
        print eq
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
        print eq
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
        print eq
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
        print(eq)
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
        print(eq)
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
        print(eq)
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
        print(eq)
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
        print(eq)
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
        print(eq)
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
        print(age)
        assert abs(age.get_val() - 13412.0) <= 0.00001
        print('Assign 05: Problem 04: Unit Test 01: pass')

    # to solve
    def test_assign_05_prob_04_ut_02(self):
        print('\n***** Assign 05: Problem 04: Unit Test 02 *****')
        age = c14_carbon_dating(make_const(0.583))
        print(age)
        assert abs(age.get_val() - 4497.0) <= 0.00001
        print('Assign 05: Problem 04: Unit Test 02: pass')

    # give as a unit test
    def test_assign_05_prob_04_ut_02(self):
        print('\n***** Assign 05: Problem 04: Unit Test 03 *****')
        age = c14_carbon_dating(make_const(0.80))
        print(age)
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
    
   
    def runTest(self):
        pass

if __name__ == '__main__':
    unittest.main()
