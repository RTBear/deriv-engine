#!/usr/bin/python

from const import const

class point2d(object):
    def __init__(self, x=const(val=0.0), y=const(val=0.0)):
        self.__x__ = x
        self.__y__ = y

    def get_x(self):
        return self.__x__

    def get_y(self):
        return self.__y__

    def __str__(self):
        assert not self.__x__ is None
        assert not self.__y__ is None
        return '(' + str(self.__x__) + ', ' + str(self.__y__) + ')'

    
