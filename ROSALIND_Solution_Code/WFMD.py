##  The Wright-Fisher Model of Genetic Drift
##  idea and main code copied from https://github.com/timothymahajan/Project-Rosalind-Bioinformatics-Stronghold/blob/master/087_WFMD/WFMD.py

import math

def binomial(n, i, m):
    return (math.factorial(n) / math.factorial(i) / math.factorial(n-i)) * ((m/n)**i * (1-(m/n))**(n-i))

def probability(N, m, g, k):
    n = N * 2+1
    current = [0]*(n)
    current[m] = 1
    for z in range(g):
        next = [0]*(n)
        for i in range(n):
            for j in range(n):
                next[i] += binomial(float(n-1), float(i), float(j)) * current[j]         
        current = next
    return sum(current[:-k])

N,m,g,k = map(int,"7 10 5 6".split(" "))
print(probability(N, m, g, k))
