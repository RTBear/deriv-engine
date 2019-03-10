#!/usr/bin/python

###########################################
# module: graph_drv.py
# Ryan Mecham
# A01839282
###########################################

from var import var
from const import const
from pwr import pwr
from prod import prod
from deriv import deriv
from plus import plus
from tof import tof
from maker import make_pwr, make_const, make_pwr_expr
from deriv import deriv
from tof import tof
import numpy as np
import matplotlib.pyplot as plt
import math

def graph_drv(fexpr, xlim, ylim):
    
    f = tof(fexpr)
    drv = deriv(fexpr)
    fderiv1 = tof(drv)

    print fexpr
    print drv

    xvals1 = np.linspace(xlim[0],xlim[1],10000)
    yvals0 = np.array([f(x) for x in xvals1])
    yvals1 = np.array([fderiv1(x) for x in xvals1])    

    fig1 = plt.figure(1)
    fig1.suptitle('Function and It\'s Derivative')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.ylim(ylim)
    plt.xlim(xlim)
    plt.grid()
    plt.plot(xvals1, yvals0, label='y=f(x)='+str(fexpr), c='r') 
    plt.plot(xvals1, yvals1, label='y=f`(x)='+str(drv), c='g')
    plt.legend(loc='best')
    plt.show()

