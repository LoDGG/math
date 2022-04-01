from sympy import *
from enum import Enum

x = symbols('x')


# data to be plotted
class function:
    def __init__(self, fx, domain):
        self.fx = fx
        self.domain = domain

    def eval(self, value):
        return self.fx.subs(x, value)


def function_graph(f):
    (inf, sup) = f.domain
    p1 = plot(f.fx, (x, inf, sup), xlim=f.domain, ylim=f.domain, show=True, legend=True, xlabel='', ylabel='',
              title='f(x)', margin=0.,
              autoscale=True)
    p1.show()


class conCX(Enum):
    CONC = 1
    NONE = 0
    CONX = -1


class sign(Enum):
    POS = 1
    NONE = 0
    NEG = -1


def d(func, n=1):
    res = function(func.fx, func.domain)
    for i in range(n):
        res.fx = res.fx.diff(x)
    return res


def isConvX(f):
    return None if d(f, 2).fx._eval_is_zero() else d(f, 2).fx.is_positive


def isIncr(f):
    return None if d(f, 2).fx._eval_is_zero() else d(f).fx.is_positive
