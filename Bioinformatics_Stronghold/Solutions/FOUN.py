##  The Founder Effect and Genetic Drift 
##  Copy the code from WFMD. only change the return of probability() 


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
                next[i] += binomial(n-1, i, j) * current[j]         
        current = next
    return current[-k]

with open("test.txt",'r') as f:
    N,m = map(int,f.readline().split())
    A = [i for i in map(int,f.readline().split())]

for x in range(1,m+1):
    print(" ".join(str(math.log(probability(N, y, x, 0),10)) for y in A))

