#!/usr/bin/python

#########################################
# module: pwr.py
# bugs to vladimir kulyukin via canvas.
#########################################

class pwr(object):
    def __init__(self, base=None, deg=None):
        self.__base__ = base
        self.__deg__  = deg

    def get_base(self):
        return self.__base__

    def get_deg(self):
        return self.__deg__

    def __str__(self):
        return '(' + str(self.__base__) + '^' + str(self.__deg__) + ')'
