#!/usr/bin/python

################################################
# module: consts.py
# bugs to vladimir kulyukin via canvas
################################################

import math
from const import const

def is_e_const(c):
  if isinstance(c, const):
    return c.get_val() == math.e
  else:
    return False

def is_zero_const(c):
  if isinstance(c, const):
    return c.get_val() == 0.0
  else:
    return False

def is_pi_const(c):
  if isnstance(c, const):
    return c.get_val() == math.pi
  else:
    return False
