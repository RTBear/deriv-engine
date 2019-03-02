#!/usr/bin/python

#####################################
# module: antideriv.py
# Ryan Mecham
# A01839282
#####################################

from var import var
from const import const
from consts import is_e_const, is_pi_const, is_zero_const
from pwr import pwr
from prod import prod
from plus import plus
from quot import quot
from ln import ln
from absv import absv
from deriv import deriv
from maker import make_const, make_pwr, make_pwr_expr, make_e_expr
from tof import is_valid_non_const_expr, is_valid_non_const_var_expr
import math


def antideriv(i):
    ## CASE 1: i is a constant
    if isinstance(i, const):
        return prod(i,make_pwr('x',1.0))
    ## CASE 2: i is a pwr
    elif isinstance(i, pwr):
        b = i.get_base()
        d = i.get_deg()
        ## CASE 2.1: b is var and d is constant.
        if isinstance(b, var) and isinstance(d, const):
            #(b^(d+1))/(d+1)
            if d.get_val() == -1.0:
                return ln(make_pwr('x',1.0))
            return quot(pwr(b,const(d.get_val()+1.0)),const(d.get_val()+1.0))
        ## CASE 2.2: b is e
        elif is_e_const(b):
            if isinstance(d, const) or isinstance(d, pwr) or isinstance(d, var) or isinstance(d, prod):
                if isinstance(d, const):
                    return prod(const(b.get_value() ** d.getvalue()), var('x'))
                elif isinstance(d, var):#e^x
                    return i
                elif isinstance(d, pwr) and d.get_deg() == 1.0:#e^x^1
                    return i
                elif isinstance(d, prod):
                    left = d.get_mult1()
                    right = d.get_mult2()
                    if isinstance(left, var) or (isinstance(left, pwr) and left.get_deg().get_val() == 1.0):
                        # e^xa == e^ax => (1/a) * e^ax
                        return prod(quot(const(1.0),right),i)
                    elif isinstance(right, var) or (isinstance(right, pwr) and right.get_deg().get_val() == 1.0):
                        # e^ax => (1/a) * e^ax
                        return prod(quot(const(1.0),left),i)
                    else:
                        raise Exception('e^(unknown expression)')
                else:
                    raise Exception('antideriv: unknown case -- did not implement substitution')
        ## CASE 2.3: b is a sum
        elif isinstance(b, plus):
            #(x+y)^d => ((x+y)^(d+1))/(d+1)
            if isinstance(d, const):
                if d.get_val() == -1.0:
                    return prod(pwr(deriv(b),const(d.get_val()+1.0)) , ln(b) )
                    # return prod(pwr(deriv(b),const(d.get_val()+1.0)) , quot(make_pwr_expr(b,const(d.get_val()+1.0)),const(d.get_val()+1.0)))
                else:
                    # return prod(pwr(deriv(b),const(d.get_val()+1.0)) , quot(make_pwr_expr(b,const(d.get_val()+1.0)),const(d.get_val()+1.0)))
                    # return prod(make_pwr_expr(prod(deriv(b),const(d.get_val()+1.0)), -1.0) , quot(make_pwr_expr(b,const(d.get_val()+1.0)),const(d.get_val()+1.0)))

                    # formula from this page (https://www.quora.com/How-do-I-find-anti-derivative-of-ax+b-2)
                    return prod(
                                make_pwr_expr(
                                    prod(
                                        deriv(b),
                                            const(d.get_val()+1.0)
                                    ),
                                    -1.0
                                ),
                                make_pwr_expr(b, const(d.get_val()+1.0))
                           )
            else:
                raise Exception('antideriv: unknown case')
        else:
            raise Exception('antideriv: unknown case')
    ### CASE 3: i is a sum, i.e., a plus object.
    elif isinstance(i, plus):
        # S(n+m) => S(n) + S(m)
        return plus(antideriv(i.get_elt1()),antideriv(i.get_elt2()))

    ### CASE 4: is is a product, i.e., prod object,
    ### where the 1st element is a constant.
    elif isinstance(i, prod):
        left = i.get_mult1()
        right = i.get_mult2()
        if isinstance(left, const):
            return prod(left,antideriv(right))
        elif isinstance(right, const):
            return prod(right,antideriv(left))
        else:
            raise Exception('antideriv: unknown case -- did not implement special rules (like substitution)')
    else:
        raise Exception('antideriv: unknown case' + str(type(i)) + str(i))

                     
            
    
    
