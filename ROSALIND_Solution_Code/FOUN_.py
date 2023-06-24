##  The Founder Effect and Genetic Drift

import math

def binomial(n, i, m):
    return (math.factorial(n) / math.factorial(i) / math.factorial(n-i)) * ((m/n)**i * (1-(m/n))**(n-i))

N,m = 4,3
A = [0,1,2]
n = 2*N

cur = [1]*len(A)

for j in range(len(A)):
    for i in range(len(A)):
        cur[i] *= binomial(float(n),float(0),float(A[i]))
    print " ".join(str(math.log(i,10)) for i in cur)

def wf_model(n, m, g):
    # transition matrix
    tmat = [[dbinom(x, n, m / n) for x in range(n + 1)] for m in range(n + 1)]
    tmat = np.array(tmat)
    v = np.array([0] * (n + 1))
    v[m] = 1
    for i in range(g):
        v = np.dot(v, tmat)
    return v


    def foun(n, m, a):
    """The Founder Effect and Genetic Drift"""
    for g in range(1, m + 1):
        yield [log10(wf_model(2 * n, i, g)[0]) for i in a]


def main(file):
    """The Founder Effect and Genetic Drift"""
    l1, l2 = Parser(file).lines()
    n, m = [int(x) for x in l1.split()]
    a = [int(x) for x in l2.split()]
    for x in foun(n, m, a):
        print(*[f"{f:.12f}" for f in x])
