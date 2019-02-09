from hw03 import maximize_revenue
from deriv import deriv
from var import var
from const import const
from pwr import pwr
from prod import prod
from plus import plus
from tof import tof
# from graphdrv import graph_drv
from maker import make_const, make_pwr, make_pwr_expr, make_prod, make_plus, make_point2d
import math
from poly12 import find_poly_1_zeros, find_poly_2_zeros
from point2d import point2d
from derivtest import loc_xtrm_1st_drv_test, loc_xtrm_2nd_drv_test

fex = plus(prod(mult1=make_const(2.0), mult2=make_pwr('x',1.0)),make_const(5.0))
print fex
# drv = deriv(fex)
# print drv

z = find_poly_1_zeros(fex)
print isinstance(z,const)
print z
#verify this is a true zero
f = tof(fex)
print 'true zero?',f(z.get_val()) == 0.0
print '------------------------------------------------------'

def test_01():
    f1 = make_prod(make_const(3.0),make_pwr('x', 1.0))
    f2 = make_plus(f1, make_const(100.0))
    print f2
    z = find_poly_1_zeros(f2)
    f2f = tof(f2)
    assert f2f(z.get_val()) == 0.0
    print str(z)
    print 'true zero?',f2f(z.get_val()) == 0.0


test_01()
print '------------------------------------------------------'
def test_02():
    f0 = make_prod(make_const(0.5), make_pwr('x', 2.0))
    f1 = make_prod(make_const(6.0), make_pwr('x', 1.0))
    f2 = make_plus(f0, f1)
    poly = make_plus(f2, make_const(0.0))
    print '+++',poly
    zeros = find_poly_2_zeros(poly)
    for c in zeros:
        print c
    pf = tof(poly)
    for c in zeros:
        assert abs(pf(c.get_val()) - 0.0) <= 0.0001
    print 'True zeros!'
test_02()
print '------------------------------------------------------'
def test_03():
    f1 = make_prod(make_const(1.0/3.0), make_pwr('x', 3.0))
    f2 = make_prod(make_const(-2.0), make_pwr('x', 2.0))
    f3 = make_prod(make_const(3.0), make_pwr('x', 1.0))
    f4 = make_plus(f1, f2)
    f5 = make_plus(f4, f3)
    poly = make_plus(f5, make_const(1.0))
    print 'f(x) = ', poly
    xtrma = loc_xtrm_1st_drv_test(poly)
    for i, j in xtrma:
        print i, str(j)
test_03()
print '------------------------------------------------------'
e1 = make_prod(make_const(1.0/12.0), make_pwr('x', 2.0))
e2 = make_prod(make_const(-10.0), make_pwr('x', 1.0))
sum1 = make_plus(e1, e2)
sum2 = plus(sum1,const(300.0))
drv = deriv(sum2)
print sum2
print drv
xtrm = loc_xtrm_2nd_drv_test(sum2)
for val in xtrm:
    print val[0]
    print val[1]
# print loc_xtrm_2nd_drv_test(drv)
num_units, rev, price = maximize_revenue(sum2)
print "num_units",num_units
print 'rev',rev
print 'price',price

print '------------------------------------------------------'
print '------------------------------------------------------'