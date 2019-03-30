#!/usr/bin/python

###############################################
# module: riemann.py
# Ryan Mecham
# A01839282
###############################################

## modify these imports as you see fit.
from __future__ import print_function
import numpy as np
from const import const
from antideriv import antiderivdef
from tof import tof
import matplotlib.pyplot as plt
from maker import make_const
from graph import *

def riemann_approx(fexpr, a, b, n, pp=0):
  '''
  fexpr: expression to be approximated
  a: lower bound
  b: upper bound
  n: number of subintervals used in approximation

  pp=  0 - approximate with reimann midpoint
  pp= +1 - approximate with reimann right point
  pp= -1 - approximate with reimann left point
  '''
  assert isinstance(a, const)
  assert isinstance(b, const)
  assert isinstance(n, const)

  a_val = a.get_val()
  b_val = b.get_val()
  n_val = n.get_val()

  #figure out size of each partition and use this for determining how to use pp

  partition_size = (b_val - a_val) / n_val

  subintervals = np.linspace(start=a_val,stop=b_val,num=n_val,endpoint=False)

  if pp == -1:
    shifted_subintervals = subintervals
  elif pp == 0:
    shifted_subintervals = map(lambda(x): x + (partition_size/2), subintervals)
  elif pp == 1:
    shifted_subintervals = map(lambda(x): x + partition_size, subintervals)

  f_fexpr = tof(fexpr)
  # print(a_val,b_val,partition_size,shifted_subintervals)
  riemann_values = map(f_fexpr, shifted_subintervals)
  riemann_values = map(lambda(x):x*partition_size, riemann_values)
  r_sum = sum(riemann_values)

  return const(r_sum)
  # return r_sum


def riemann_approx_with_gt(fexpr, a, b, gt, n_upper, pp=0):
  assert isinstance(a, const)
  assert isinstance(b, const)
  assert isinstance(gt, const)
  assert isinstance(n_upper, const)

  res = [( n_i, const( abs(riemann_approx(fexpr,a,b,const(n_i),pp).get_val() - gt.get_val()) ) ) for n_i in range(1,n_upper.get_val())]

  ''' below is a less obfuscated method of getting res (but is not on one line :(   ) '''
  # res = []
  # for n_i in range(1,n_upper.get_val()):
  #   r_sum = riemann_approx(fexpr, a, b, const(n_i), pp)
  #   res.append( (n_i, const( abs(r_sum.get_val() - gt.get_val()) ) ) )

  return res


def plot_riemann_error(fexpr, a, b, gt, n):
  assert isinstance(a, const)
  assert isinstance(b, const)
  assert isinstance(gt, const)
  assert isinstance(n, const)

  left = riemann_approx_with_gt(fexpr, a, b, gt, n, pp=-1)
  middle = riemann_approx_with_gt(fexpr, a, b, gt, n, pp=0)
  right = riemann_approx_with_gt(fexpr, a, b, gt, n, pp=1)

  graph_riemann_approx_err(approxs=(right,left,middle),xmin=a.get_val(),xmax=b.get_val(),n=n.get_val(),name='Riemann Approximation Error')



