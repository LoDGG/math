import random

from tool import *
from random import *


def generateSet(a, b, c, d, e, n):
    xiSet = []
    for i in range(n):
        xiSet.append(uniform(a, b))
    xiSet.sort()

    N = [(xiSet[0], uniform(c, d))]
    for i in range(1, n):
        pnt = N[i - 1][1] + (uniform(max(-e, -(N[i - 1][1] - c)), min(e, d - N[i - 1][1])))
        # Previous pnt ↑   +  rand(e,-e) or  less if yi is next to a bound (c or d)
        N.append((xiSet[i], pnt))
    return N


def variationCount(N):
    incr = 0
    count = 0
    for i in range(1,len(N)):

        if N[i][1] < N[i - 1][1] and incr != -1:
            count += 1
            incr = -1

        elif N[i][1] > N[i - 1][1] and incr != 1:
            count += 1
            incr = 1

        elif N[i][1] == N[i - 1][1] and incr != 0:
            count += 1
            incr = 0
    return count


def matC(N, n):
    C = []
    for i in range(n + 1):
        sum = 0
        for k in range(len(N)):
            sum += N[k][1] * N[k][0] ** i
        C.append(sum)
    return Matrix(C)

def matA(N,n):
    A = []
    for i in range(n+1):
        A.append([0]*(n+1))

    for i in range(n + 1):
        for j in range(n + 1):
            j = n if i != 0 else j
            sum = 0
            for k in range(len(N)):
                sum += N[k][0] ** (i + j)
            A[i][j] = sum

    for i in range(1,len(A)):
        for j in range(len(A)-1):
            A[i][j] = A[i-1][j+1]
    return Matrix(A)


def LeastSquareMath(N):

    deg = variationCount(N)
    A = matA(N,deg)
    C = matC(N,deg)
    coeff = A**-1 * C
    return coeff


def graphPoly(M):
    P = function(0,(-100,100))
    for i in range(shape(M)[0]):
        P.fx+= M[i,0]*x**i
    print(M)

    plot(P.fx, (x, P.domain[0], P.domain[1]), xlim=P.domain, ylim=P.domain, show=True, legend=False, xlabel='', ylabel='',
              title='f(x)', margin=0.,
              autoscale=True)
    return P




"""          ----------- Testing CODE : -------------------          """

mySet = generateSet(0, 20, 5, 10, 3, 10)
print(mySet)
print(Sum(x, (x, 0, 9)).doit())
N = [(0, 7), (1, 4), (2, 2), (4, 4), (6, 12)]
N = [(0, 2),(1, 1),(2, 0),(3,-1),(4, -3),(6, -1),(7, 0),(9, 2),(11, 4),(12, 5),(15, 7),(16, 10),(17,8),(18, -3),(20, -10)]
N = [(-12,9),(0,0),(2,0.1),(5.2,31),(10,18),(24,15),(25,1),(31,31),]
print(variationCount(N))
graphPoly(LeastSquareMath(N))


