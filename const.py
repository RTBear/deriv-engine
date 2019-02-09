#!/usr/bin/python

########################################
# module: const.py
# bugs to vladimir kulyukin via canvas.
########################################

class const(object):
    def __init__(self, val=0.0):
        self.__val__ = val

    def get_val(self):
        return self.__val__

    def __str__(self):
        return str(self.__val__)

    @staticmethod
    def add(c1, c2):
        assert isinstance(c1, const)
        assert isinstance(c2, const)
        v1, v2 = c1.get_val(), c2.get_val()
        return const(val=(v1 + v2))

    @staticmethod
    def mult(c1, c2):
        assert isinstance(c1, const)
        assert isinstance(c2, const)
        v1, v2 = c1.get_val(), c2.get_val()
        return const(val=(v1 * v2))

    @staticmethod
    def divide(c1, c2):
        assert isinstance(c1, const)
        assert isinstance(c2, const)
        v1, v2 = c1.get_val(), c2.get_val()
        return const(val=(v1 / v2))

