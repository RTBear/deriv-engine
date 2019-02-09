#!/usr/bin/python

# absv stands for "absolute value."
# objects of this class represent absolute values of
# mathematical expressions.
#
# use example:
# >>> from make import make_const
# >>> c = make_const(5.0)
# >>> print(absv(c))
# >>> |5.0|
# >>> from maker import make_pwr
# >>> fex = make_pwr('x', 5.0)
# >>> print(absv(fex))
# |(x^5.0)|
# >>> print(absv(fex).get_expr())
# (x^5.0)
# bugs to vladimir kulyukin via canvas.

class absv(object):
    def __init__(self, expr):
        self.__expr__ = expr

    def get_expr(self):
        return self.__expr__

    def __str__(self):
        return '|' + str(self.__expr__) + '|'

