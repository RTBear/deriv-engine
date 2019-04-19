#!/usr/bin/python

###################################
# module: linprog.py
# Ryan Mecham
# A01839282
###################################

## your imports
from line_eq import line_eq
from maker import make_line_eq
from maker import make_var, make_const, make_prod
from maker import make_pwr, make_plus
from maker import make_point2d
from const import const
from var import var
from prod import prod
from pwr import pwr
# from poly12 import is_pwr_1
from plus import plus
from tof import tof
import sys
import numpy as np
'''
'''


### sample line equations
lneq1 = make_line_eq(make_var('y'),
                                    make_const(2))
lneq2 = make_line_eq(make_var('y'),
                                    make_var('x'))
lneq3 = make_line_eq(make_var('y'),
                                    make_var('y'))
lneq4 = make_line_eq(make_var('y'),
                                    make_prod(make_const(2.0),
                                                        make_pwr('x', 1.0)))
lneq5 = make_line_eq(make_var('y'),
                                    make_prod(make_const(5.0),
                                                        make_pwr('y', 1.0)))
lneq6 = make_line_eq(make_var('y'),
                                    make_plus(make_prod(make_const(5.0),
                                                                        make_pwr('x', 1.0)),
                                                    make_const(4.0)))
lneq7 = make_line_eq(make_var('y'),
                                    make_plus(make_prod(make_const(5.0),
                                                                        make_pwr('y', 1.0)),
                                                    make_const(4.0)))
lneq8 = make_line_eq(make_var('y'),
                                    make_plus(make_prod(make_const(3.0),
                                                                        make_pwr('x', 1.0)),
                                                    make_const(-4.0)))

def get_line_coeffs(lneq):
    lhs = lneq.get_lhs()
    rhs = lneq.get_rhs()

    #print('lhs',str(lhs), type(lhs))
    #print('rhs',str(rhs), type(rhs))

    x,y,c = 0,0,0

    lvar = checkForVar(lhs)#check lhs for plain variable
    if lvar == 'y':
        y = 1
    elif lvar == 'x':
        x = 1

    rvar = checkForVar(rhs)#check rhs for plain variable
    if rvar == 'y':
        y = -1
    elif rvar == 'x':
        x = -1


    if isinstance(lhs, const):#check lhs for constant
        # print('lhs const',str(lhs))
        c = -lhs.get_val()

    if isinstance(rhs, const):#check rhs for constant
        # print('rhs const',str(rhs))
        c = rhs.get_val()

    ###############################
    #### CHECK rhs FOR product ####
    ###############################
    if isinstance(rhs, prod):#check rhs for product
        #print('rhs prod')
        left = rhs.get_mult1()
        right = rhs.get_mult2()

        assert isinstance(left, const) or isinstance(right, const)

        lvar = checkForVar(left)#check left for plain variable
        if lvar == 'y':
            y = right.get_val()
        elif lvar == 'x':
            x = right.get_val()

        rvar = checkForVar(right)#check right for plain variable
        if rvar == 'y':
            y = -left.get_val()
        elif rvar == 'x':
            x = -left.get_val()

    ###############################
    #### CHECK lhs FOR product ####
    ###############################
    if isinstance(lhs, prod):#check lhs for product
        #print('lhs prod')
        left = lhs.get_mult1()
        right = lhs.get_mult2()

        assert isinstance(left, const) or isinstance(right, const)

        lvar = checkForVar(left)#check left for plain variable
        if lvar == 'y':
            y = right.get_val()
        elif lvar == 'x':
            x = right.get_val()

        rvar = checkForVar(right)#check right for plain variable
        if rvar == 'y':
            y = -left.get_val()
        elif rvar == 'x':
            x = -left.get_val()

    ############################
    #### CHECK RHS FOR PLUS ####
    ############################
    if isinstance(rhs, plus):
        #print('rhs plus')
        pleft = rhs.get_elt1()
        pright = rhs.get_elt2()
        #print('pleft',str(pleft),type(pleft))
        #print('pright',str(pright),type(pright))

        lvar = checkForVar(pleft)#check pleft for plain variable
        if lvar == 'y':
            y = -1
        elif lvar == 'x':
            x = -1

        rvar = checkForVar(pright)#check pright for plain variable
        if rvar == 'y':
            y = -1
        elif rvar == 'x':
            x = -1

        if isinstance(pright, prod):#check pright for product
            #print('pright, prod')

            left = pright.get_mult1()
            right = pright.get_mult2()

            assert isinstance(left, const) or isinstance(right, const)

            lvar = checkForVar(left)#check left for plain variable
            if lvar == 'y':
                y = -right.get_val()
            elif lvar == 'x':
                x = -right.get_val()

            rvar = checkForVar(right)#check right for plain variable
            if rvar == 'y':
                y = -left.get_val()
            elif rvar == 'x':
                x = -left.get_val()

        if isinstance(pleft, prod):#check pleft for product
            #print('pleft, prod')

            left = pleft.get_mult1()
            right = pleft.get_mult2()

            assert isinstance(left, const) or isinstance(right, const)

            lvar = checkForVar(left)#check left for plain variable
            if lvar == 'y':
                y = -right.get_val()
            elif lvar == 'x':
                x = -right.get_val()

            rvar = checkForVar(right)#check right for plain variable
            if rvar == 'y':
                y = -left.get_val()
            elif rvar == 'x':
                x = -left.get_val()

        if isinstance(pleft, const):#check lhs for constant
            # #print('lhs const',str(lhs))
            c = pleft.get_val()

        if isinstance(pright, const):#check rhs for constant
            # #print('rhs const',str(rhs))
            c = pright.get_val()

    ############################
    #### CHECK LHS FOR PLUS ####
    ############################
    if isinstance(lhs, plus):
        #print('lhs plus')
        pleft = lhs.get_elt1()
        pright = lhs.get_elt2()

        lvar = checkForVar(pleft)#check pleft for plain variable
        if lvar == 'y':
            y = 1
        elif lvar == 'x':
            x = 1

        rvar = checkForVar(pright)#check pright for plain variable
        if rvar == 'y':
            y = 1
        elif rvar == 'x':
            x = 1

        if isinstance(pright, prod):#check pright for product
            left = pright.get_mult1()
            right = pright.get_mult2()

            assert isinstance(left, const) or isinstance(right, const)

            lvar = checkForVar(left)#check left for plain variable
            if lvar == 'y':
                y = right.get_val()
            elif lvar == 'x':
                x = right.get_val()

            rvar = checkForVar(right)#check right for plain variable
            if rvar == 'y':
                y = left.get_val()
            elif rvar == 'x':
                x = left.get_val()

        if isinstance(pleft, prod):#check pleft for product
            left = pleft.get_mult1()
            right = pleft.get_mult2()

            assert isinstance(left, const) or isinstance(right, const)

            lvar = checkForVar(left)#check left for plain variable
            if lvar == 'y':
                y = right.get_val()
            elif lvar == 'x':
                x = right.get_val()

            rvar = checkForVar(right)#check right for plain variable
            if rvar == 'y':
                y = left.get_val()
            elif rvar == 'x':
                x = left.get_val()

        if isinstance(pleft, const):#check lhs for constant
            # #print('lhs const',str(lhs))
            c = -pleft.get_val()

        if isinstance(pright, const):#check rhs for constant
            # #print('rhs const',str(rhs))
            c = -pright.get_val()

    #print('---xyc---')
    #print(x,y,c)
    #print('---------')
    return (x, y, c)

def checkForVar(expr):
    if isinstance(expr, var):#check rhs for plain variable
        return str(expr)
    elif isinstance(expr, pwr):
        base = expr.get_base()
        assert isinstance(base, var)
        return str(base)
    else:
        return None

def line_intersection(lneq1, lneq2):
    e1_x, e1_y, e1_c = get_line_coeffs(lneq1)
    e2_x, e2_y, e2_c = get_line_coeffs(lneq2)

    A = np.array([[e1_x, e1_y],
                  [e2_x, e2_y]])
    b = np.array([e1_c, e2_c])

    # print(A)
    # print(b)
    try:
        pt = np.linalg.solve(A,b)
    except:
        return None
    
    return make_point2d(pt[0], pt[1])
### a few tests

def test_01():
    ln1 = make_line_eq(make_var('y'), make_const(1.0))
    ln2 = make_line_eq(make_var('x'), make_const(1.0))
    # assert is_const_line(ln1)
    # assert is_const_line(ln2)
    print(line_intersection(ln1, ln2))

def test_02():
    ln1 = make_line_eq(make_var('y'), make_const(2.0))
    ln2 = make_line_eq(make_var('y'), make_plus(make_pwr('x', 1.0),
                                                                    make_const(-6.0)))
    print(line_intersection(ln1, ln2))
    print(line_intersection(ln2, ln1))

def test_03():
    ln1 = make_line_eq(make_var('y'), make_const(-2.0))
    ln2 = make_line_eq(make_var('y'), make_plus(make_pwr('x', 1.0),
                                                                    make_const(10.0)))
    print(line_intersection(ln1, ln2))
    print(line_intersection(ln2, ln1))

def test_04():
    ln1 = make_line_eq(make_var('y'), make_const(2.0))
    ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(2.0),
                                                                            make_pwr('x', 1.0)),
                                                                        make_const(-6.0)))
    print(line_intersection(ln1, ln2))
    print(line_intersection(ln2, ln1))

def test_05():
    ln1 = make_line_eq(make_var('y'), make_pwr('x', 1.0))
    ln2 = make_line_eq(make_var('y'), make_prod(make_const(2.0),
                                                                 make_pwr('x', 1.0)))
    ln3 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(3.0),
                                                                            make_pwr('x', 1.0)),
                                                                    make_const(-10.0)))
    print(get_line_coeffs(ln1))
    print(get_line_coeffs(ln2))
    print(get_line_coeffs(ln3))

    print(line_intersection(ln1, ln2))
    print(line_intersection(ln2, ln3))
    print(line_intersection(ln1, ln3))

def test_06():
    ln1 = make_line_eq(make_var('y'), make_pwr('x', 1.0))
    ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0),
                                                                            make_pwr('x', 1.0)),
                                                        make_const(6.0)))
    print(line_intersection(ln1, ln2))

def test_07():
    ln1 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0/5.0),
                                                                                make_pwr('x', 1.0)),
                                                            make_const(10.0)))
    ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(1.0/5.0),
                                                                                make_pwr('x', 1.0)),
                                                            make_const(5.0)))
    print(line_intersection(ln1, ln2))

def test_08():
    ln1 = make_line_eq(make_var('y'), make_const(1.0))
    ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0),
                                                                            make_pwr('x', 1.0)),
                                                        make_const(6.0)))
    print(line_intersection(ln1, ln2))

def test_09():
    ln1 = make_line_eq(make_var('y'), make_const(5.0))
    ln2 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-1.0),
                                                                            make_pwr('x', 1.0)),
                                                        make_const(6.0)))
    print(line_intersection(ln1, ln2))

def maximize_obj_fun(f, corner_points):
    mx = -9999999
    mx_pt = None
    for pt in corner_points:
        x = pt.get_x().get_val()
        y = pt.get_y().get_val()
        
        val = f(x,y)

        if val > mx:
            mx = val
            mx_pt = (x,y)
    assert not mx_pt == None

    return (mx, mx_pt)

def minimize_obj_fun(f, corner_points):
    mn = 9999999
    mn_pt = None
    for pt in corner_points:
        x = pt.get_x().get_val()
        y = pt.get_y().get_val()
        
        val = f(x,y)

        if val < mn:
            mn = val
            mn_pt = (x,y)
    assert not mn_pt == None

    return (mn, mn_pt)

def test_10():
    f1 = lambda x, y: 2*x + y
    corner_points = [make_point2d(1, 1),
                                     make_point2d(1, 5),
                                     make_point2d(5, 1)]
    print(maximize_obj_fun(f1, corner_points))                            
    f2 = lambda x, y: x - 2*y
    print(minimize_obj_fun(f2, corner_points))
    
### more tests

def test_11():
    ln1 = make_line_eq(make_var('x'), make_const(1.0))
    ln2 = make_line_eq(make_var('y'), make_prod(make_const(0.5),
                                                                make_pwr('x', 1.0)))
    print(line_intersection(ln1, ln2))
    ln3 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-3.0/4),
                                                                            make_pwr('x', 1.0)),
                                                        make_const(3.0)))
    print(line_intersection(ln1, ln3))
    print(line_intersection(ln2, ln3))


def test_12():
    ln1 = make_line_eq(make_var('x'), make_const(0.0))
    ln2 = make_line_eq(make_var('y'), make_const(0.0))
    ln3 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-4.0/3),
                                                                            make_pwr('x', 1.0)),
                                                        make_const(160.0)))
    ln4 = make_line_eq(make_var('y'), make_plus(make_prod(make_const(-0.5),
                                                                            make_pwr('x', 1.0)),
                                                        make_const(120.0)))
    print(ln1)
    print(ln3)
    print(line_intersection(ln1, ln3))
    print(ln2)
    print(ln3)
    print(line_intersection(ln2, ln3))
    print(line_intersection(ln3, ln4))

## write your answer to problem 1a as x, y, mv
#ANSWER: 5, 1, 11
def opt_prob_1a():
    f1 = lambda x, y: 2*x + y


    #find corner points:
    ln1 = make_line_eq(make_var('x'), make_const(1.0))
    ln2 = make_line_eq(make_var('y'), make_const(1.0))

    ln3 = make_line_eq(make_var('x'), make_const(5.0))
    ln4 = make_line_eq(make_var('y'), make_const(5.0))

    p12 = line_intersection(ln1, ln2)
    # p13 = line_intersection(ln1, ln3) #parallel lines
    p14 = line_intersection(ln1, ln4)

    p23 = line_intersection(ln2, ln3)
    # p24 = line_intersection(ln2, ln4) #parallel lines

    p34 = line_intersection(ln3, ln4)

    possible_cps = [p12,p14,p23,p34]

    corner_points = [pt for pt in possible_cps if pt.get_x().get_val() + pt.get_y().get_val() <= 6] #x+y <= 6

    # for pt in corner_points:
    #     print(pt.get_x().get_val(), pt.get_y().get_val())

    print '1a: ',maximize_obj_fun(f1, corner_points)

## write your answer to problem 1b as x, y, mv
#ANSWER: 2, 2, 3
def opt_prob_1b():
    f1 = lambda x, y: x/2 + y

    #find corner points:
    ln1 = make_line_eq(make_var('x'), make_const(0.0))
    ln2 = make_line_eq(make_var('y'), make_const(2.0))

    ln3 = make_line_eq(make_var('x'), make_var('y'))#x=y
    ln4 = make_line_eq(make_plus(make_var('x'),make_var('y')), make_const(6.0))# x+y=6


    p12 = line_intersection(ln1, ln2)
    p13 = line_intersection(ln1, ln3)
    p14 = line_intersection(ln1, ln4)

    p23 = line_intersection(ln2, ln3)
    p24 = line_intersection(ln2, ln4)

    p34 = line_intersection(ln3, ln4)

    possible_cps = [p12,p13,p14,p23,p24,p34]

    # for pt in possible_cps:
    #     print pt

    corner_points = [pt for pt in possible_cps if pt.get_x().get_val() + pt.get_y().get_val() <= 6] #x+y <= 6
    corner_points = [pt for pt in corner_points if pt.get_x().get_val() >= pt.get_y().get_val()] #x>=y
    corner_points = [pt for pt in corner_points if pt.get_x().get_val() >= 0] #x>=0
    corner_points = [pt for pt in corner_points if pt.get_y().get_val() >= 2] #y>=2


    # for pt in corner_points:
    #     print(pt.get_x().get_val(), pt.get_y().get_val())

    print '1b: ',minimize_obj_fun(f1, corner_points)

## write your answer to problem 1c as x, y, mv
#ANSWER: 2.5, 2.5, 2.5
def opt_prob_1c():
    f1 = lambda x, y: 3*x - 2*y


    #find corner points:
    ln1 = make_line_eq(make_plus(make_var('x'),make_var('y')), make_const(0.0))# x+y=0
    ln2 = make_line_eq(make_var('x'),make_var('y'))# x-y=0 => x=y
    ln3 = make_line_eq(make_plus(make_prod(make_const(-2.0), make_var('x')),make_prod(make_const(4.0), make_var('y'))), make_const(5.0))# -2x+4y=5


    p12 = line_intersection(ln1, ln2)
    p13 = line_intersection(ln1, ln3)

    p23 = line_intersection(ln2, ln3)


    possible_cps = [p12,p13,p23]

    corner_points = [pt for pt in possible_cps if -2*pt.get_x().get_val() + 4*pt.get_y().get_val() <= 5] # -2x+4y<=5
    corner_points = [pt for pt in corner_points if pt.get_x().get_val() + pt.get_y().get_val() >= 0] #x+y>=0
    corner_points = [pt for pt in corner_points if pt.get_x().get_val() - pt.get_y().get_val() <= 0] #x-y<=0

    # for pt in corner_points:
    #     print(pt.get_x().get_val(), pt.get_y().get_val())

    print '1c: ',maximize_obj_fun(f1, corner_points)
    

if __name__ == '__main__':
    #all good tests through test 9
    # print('#################################################################1')                                               
    test_01()           
    # print('#################################################################2')                                               
    # test_02()
    # print('#################################################################3')                                               
    # test_03()
    # print('#################################################################4')                                               
    # test_04()
    # print('#################################################################5')                                               
    # test_05()
    # print('#################################################################6')                                               
    # test_06()
    # print('#################################################################7')                                               
    # test_07()
    # print('#################################################################8')                                               
    # test_08()
    # print('#################################################################9')                                               
    # test_09()

    opt_prob_1a()
    opt_prob_1b()
    opt_prob_1c()
