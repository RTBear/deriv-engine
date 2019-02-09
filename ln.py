#!/usr/bin/python

# bugs to vladimir kulyukin on canvas.

class ln(object):
    def __init__(self, expr=None):
        self.__expr__ = expr

    def get_expr(self):
        return self.__expr__

    def __str__(self):
        return 'ln' + str(self.__expr__) 
