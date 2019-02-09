#!/usr/bin/python

#########################################
# module: plus.py
# bugs to vladimir kulyukin via canvas.
#########################################

class plus(object):
    def __init__(self, elt1=None, elt2=None):
        self.__elt1__ = elt1
        self.__elt2__ = elt2

    def get_elt1(self):
        return self.__elt1__

    def get_elt2(self):
        return self.__elt2__

    def __str__(self):
        return '(' + str(self.__elt1__) + '+' + str(self.__elt2__) + ')'
