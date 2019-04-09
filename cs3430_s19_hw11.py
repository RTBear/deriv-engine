#!/usr/bin/python

########################################
# module: cs3430_s19_hw11.py
# Ryan Mecham
# A01839282
########################################

## add your imports here
import math
from PIL import Image
import sys
import numpy as np
import cv2
from tof import tof
from const import const
from var import var
from pwr import pwr
from maker import make_const, make_pwr, make_prod, make_quot
from maker import make_plus, make_ln, make_absv
from maker import make_pwr_expr, make_e_expr
from plus import plus
from prod import prod
from deriv import deriv
'''
'''

################# Problem 1 (1 point) ###################

def nra(poly_fexpr, g, n):
    '''
    x_n = x_{n-1} + ( f(x_{n-1}) / f`(x_{n-1}) )
    '''
    assert isinstance(g, const)
    assert isinstance(n, const)


    f = tof(poly_fexpr)
    drv = deriv(poly_fexpr)
    # print('drv',str(drv))
    fprime = tof(drv)

    x_n_1 = 0
    x_n = g.get_val()
    for x in range(n.get_val()):#iterative solution
        x_n_1 = x_n
        x_n = x_n_1 - f(x_n_1) / fprime(x_n_1)
        # print('x-1',x_n_1)
        # print('x'+str(x), x_n)

    
    return x_n


################# Unit Tests for Problem 1 ###################
def nra_ut_00():
    ''' Approximating x^3 - x - 2. '''
    fexpr = make_pwr('x', 3.0)
    fexpr = make_plus(fexpr, make_prod(make_const(-1.0),
                                  make_pwr('x', 1.0)))
    fexpr = make_plus(fexpr, make_const(-2.0))
    # print('fexpr',str(fexpr))
    print(nra(fexpr, make_const(1.0), make_const(10)))

def nra_ut_01():
    ''' Approximating x^2 - 2 = 0. '''
    fexpr = make_plus(make_pwr('x', 2.0),
                      make_const(-2.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_02():
    ''' Approximating x^2 - 3 = 0. '''
    fexpr = make_plus(make_pwr('x', 2.0),
                      make_const(-3.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_03():
    ''' Approximating x^2 - 5 = 0. '''
    fexpr = make_plus(make_pwr('x', 2.0),
                      make_const(-5.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_04():
    ''' Approximating x^2 - 7 = 0. '''
    fexpr = make_plus(make_pwr('x', 2.0),
                      make_const(-7.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_05():
    ''' Approximating e^-x = x^2. '''
    fexpr = make_e_expr(make_prod(make_const(-1.0),
                                  make_pwr('x', 1.0)))
    fexpr = make_plus(fexpr,
                      make_prod(make_const(-1.0),
                                make_pwr('x', 2.0)))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_06():
    ''' Approximating 11^{1/3}.'''
    fexpr = make_pwr('x', 3.0)
    fexpr = make_plus(fexpr,
                      make_const(-11.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_07():
    ''' Approximating 6^{1/3}.'''
    fexpr = make_pwr('x', 3.0)
    fexpr = make_plus(fexpr,
                      make_const(-6.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_08():
    ''' Approximating x^3 + 2x + 2. '''
    fexpr = make_pwr('x', 3.0)
    fexpr = make_plus(fexpr,
                      make_prod(make_const(2.0),
                                make_pwr('x', 1.0)))
    fexpr = make_plus(fexpr, make_const(2.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_09():
    ''' Approximating x^3 + x - 1. '''
    fexpr = make_pwr('x', 3.0)
    fexpr = make_plus(fexpr, make_pwr('x', 1.0))
    fexpr = make_plus(fexpr, make_const(-1.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))

def nra_ut_10():
    ''' Approximating e^(5-x) = 10 - x. '''
    fexpr = make_e_expr(make_plus(make_const(5.0),
                                  make_prod(make_const(-1.0),
                                            make_pwr('x', 1.0))))
    fexpr = make_plus(fexpr, make_pwr('x', 1.0))
    fexpr = make_plus(fexpr, make_const(-10.0))
    print(nra(fexpr, make_const(1.0), make_const(10000)))


# =================== Problem 2 (4 points) ===================

def ht_detect_lines(img_fp, magn_thresh=20, spl=20):
    ## your code here
    pass

################ Unit Tests for Problem 2 ####################
##        
## I used Image for edge detection and numpy image representation
## to draw lines. Hence, I am using cv2.imwrite to save the
## image with drawn line (lnimg) and image.save to save the image
## with the edges. Feel free to modify but keep the signatures
## of these tests the same.
        
def ht_test_01(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im01_ln.png', lnimg)
    edimg.save('im01_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_02(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im02_ln.png', lnimg)
    edimg.save('im02_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_02(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im03_ln.png', lnimg)
    edimg.save('im03_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_04(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im04_ln.png', lnimg)
    edimg.save('im04_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_05(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im05_ln.png', lnimg)
    edimg.save('im05_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_06(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im06_ln.png', lnimg)
    edimg.save('im06_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_07(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im07_ln.png', lnimg)
    edimg.save('im07_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_08(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im08_ln.png', lnimg)
    edimg.save('im08_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_09(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im09_ln.png', lnimg)
    edimg.save('im09_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_10(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im10_ln.png', lnimg)
    edimg.save('im10_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_11(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im11_ln.png', lnimg)
    edimg.save('im11_ed.png')
    del img
    del lnimg
    del edimg

def ht_test_12(img_fp, magn_thresh=20, spl=20):
    img, lnimg, edimg, ht = ht_detect_lines(img_fp,
                                            magn_thresh=magn_thresh,
                                            spl=spl)
    cv2.imwrite('im12_ln.png', lnimg)
    edimg.save('im12_ed.png')
    del img
    del lnimg
    del edimg
    
if __name__ == '__main__':
    for i in range(10):
        s = 'nra_ut_0' + str(i)
        print(s)
        globals()[s]()

