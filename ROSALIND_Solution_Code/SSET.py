##  Counting Subsets

import math 

def factorial(m,n,mod = 1000000):
    result = 1
    for i in range(m,m-n,-1):
        if i ==0:
            break
        result *= i
        if result>mod:
            result %= mod
    return result

def subset(n, mod=1000000):
    total = 1
    for i in range(1,(n-1)//2+1):
        total += factorial(n,i,mod)/factorial(i,i,mod)
        if total>mod:
            result %=mod

    if n%2:
        return int(2*total%mod)
    else:
        i = n//2
        return int(2*total+factorial(n,i,mod)/factorial(i,i,mod)%mod)
        
#print(factorial(424,424))
#print(subset(848))
#for i in range(5,1,-1):
    # print(i)


for i in range(1000):
    print(i,factorial(i,i))