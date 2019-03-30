#!/usr/bin/python

###########################################
# module: graph.py
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
from graphdrv import graph_drv
import numpy as np
import matplotlib.pyplot as plt
import math

def get_matplotlib_color(index=0):
    color_options = [
        'r',#red
        'g',#green
        'b',#blue
        'c',#cyan
        'm',#magenta
        'y',#yellow
        'k',#black
        'w'#white
        ]
    return color_options[index % len(color_options)]

def graph_funcs(fexprs, xlim, ylim, name='Graph of f(x)'):
    '''
    fexprs is a iterable type containing symbolic representations of functions TODO: make a graph_lmda function that takes a lambda function instead
    xlim is a iterable type containing max/min x values
    ylim is a iterable type containing max/min y values
    '''
    for i,fexpr in enumerate(fexprs):
        f = tof(fexpr)

        xvals1 = np.linspace(xlim[0],xlim[1],10000)
        yvals0 = np.array([f(x) for x in xvals1])

        fig1 = plt.figure(1)
        fig1.suptitle(name)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.ylim(ylim)
        plt.xlim(xlim)
        plt.plot(xvals1, yvals0, label='y=f(x)='+str(fexpr), c=get_matplotlib_color(i)) 
    plt.grid()
    plt.legend(loc='best')
    plt.show()

def graph_riemann_approx_err(approxs, xmin=-10, xmax=10, n=10, name='Graph of f(x)'):
    '''
    approxs is a iterable type containing iterable types that contain points for approximations of functions
    xlim is a iterable type containing max/min x values
    ylim is a iterable type containing max/min y values
    '''
    for i,approx in enumerate(approxs):
        xvals1 = np.linspace(start=xmin,stop=xmax,num=n,endpoint=False)
        xvals1 = xvals1[1:]#trim off first element from x cuz y doesn't have it
        yvals0 = [a.get_val() for (x,a) in approx]

        fig1 = plt.figure(1)
        fig1.suptitle(name)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.ylim((min(yvals0),max(yvals0)))
        plt.xlim((xmin,xmax))
        plt.plot(xvals1, yvals0, label='y=f(x)='+['right','left','middle'][i%3], c=get_matplotlib_color(i)) 
    plt.grid()
    plt.legend(loc='best')
    plt.show()

def graphFromTable(xvals, data, labels, name=''):
    '''
    xvals: iterable where each entry is an x coordinate
    data: iterable of iterable(s). Each inner iterable is a set of y coordinates for the corisponding x coords in xvals
    labels: labels for each set in data
    '''

    ymin = 0
    ymax = 0
    for i,dataset in enumerate(data):
        fig1 = plt.figure(1)
        fig1.suptitle(name)
        plt.xlabel('x')
        plt.ylabel('y')
        ymin = min(ymin, min(dataset))
        ymax = max(ymax, max(dataset))
        plt.ylim((ymin,ymax))
        plt.xlim((min(xvals),max(xvals)))
        plt.plot(xvals, dataset, label=''+labels[i], c=get_matplotlib_color(i)) 
    plt.grid()
    plt.legend(loc='best')
    plt.show()
