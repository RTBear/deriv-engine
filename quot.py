#!/usr/bin/python

# bugs to vladimir kulyukin on canvas.

class quot(object):
    def __init__(self, num=None, denom=None):
        self.__num__ = num
        self.__denom__ = denom

    def get_num(self):
        return self.__num__

    def get_denom(self):
        return self.__denom__

    def __str__(self):
        return '(' + str(self.__num__) + '/' + str(self.__denom__) + ')'
