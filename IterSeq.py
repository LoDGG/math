import f as f

from tool import *


def LagrangeSeq(f, a, b, p1, n):
    if n == 0:
        return a
    xn = LagrangeSeq(f, a, b, p1, n - 1)

    y = ((f.eval(b) - f.eval(xn)) / (b - xn)) * (x - xn) + f.eval(xn)
    plo1 = plot(y, (x, a, b), show=False, legend=True, xlabel='', ylabel='', title='f(x)', margin=0., autoscale=True,
                axis_center='center')
    p1.extend(plo1)

    return xn - f.eval(xn) * ((b - xn) / (f.eval(b) - f.eval(xn)))


def NewtonSeq(f, x0, p1, n):
    if n == 0:
        return x0
    xn = NewtonSeq(f, x0, p1, n - 1)
    y = d(f).eval(xn) * (x - xn) + f.eval(xn)
    plo1 = plot(y, (x, 0, x0), show=False, legend=True, xlabel='', ylabel='', title='f(x)', margin=0., autoscale=True)
    p1.extend(plo1)
    return xn - f.eval(xn) / d(f).eval(xn)


def TVI(f):
    roots = list(solveset(Eq(d(f, 2).fx, 0)))

    for i in range(len(roots)):
        if roots[i] <= f.domain[0] or roots[i] >= f.domain[1]:
            roots.remove(i)

    roots.insert(0, f.domain[0])
    roots.append(f.domain[1])

    intrvList = []
    for i in range(len(roots) - 1):
        intrvList.append(Interval(roots[i], roots[i + 1]))

    for itv in intrvList:
        fitv = Interval(f.eval(itv.inf), f.eval(itv.sup)) \
            if f.eval(itv.inf) < f.eval(itv.sup) \
            else Interval(f.eval(itv.sup), f.eval(itv.inf))

        if 0 in fitv:
            return itv.inf, itv.sup


def LagrangeMeth(f, n):
    (a, b) = TVI(f)

    p1 = plot(f.fx, (x, f.domain[0], f.domain[1]), show=False, legend=True, xlabel='', ylabel='', title='f(x)',
              margin=0.,
              autoscale=True)

    res = LagrangeSeq(f, a, b, p1, n) if f.eval(b) * (d(f, 2)).eval(b) > 0 else LagrangeSeq(f, b, a, p1, n)
    p1
    p1.show()
    return res


def NewtonMeth(f, n):
    (a, b) = TVI(f)

    p1 = plot(f.fx, (x, f.domain[0], f.domain[1]), show=False, legend=True, xlabel='', ylabel='', title='f(x)',
              margin=0.,
              autoscale=True)

    res = NewtonSeq(f, b, p1, n) if f.eval(b) * (d(f, 2)).eval(b) > 0 else NewtonSeq(f, a, p1, n)
    p1.show()
    return res



"""          ----------- Testing CODE : -------------------          """

f = function(3.775*x ** 3 -3.6* x**2 + 0.5878*x -0.022, (-10, 10))

# function_graph(f)
function_graph(f)
# print(NewtonMeth(f, 3))
