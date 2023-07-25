##  Introduction to Alternative Splicing 

"""
Problem
In “Counting Subsets”, we saw that the total number of subsets of a set S
 containing n
 elements is equal to 2n
.

However, if we intend to count the total number of subsets of S
 having a fixed size k
, then we use the combination statistic C(n,k)
, also written (nk)
.

Given: Positive integers n
 and m
 with 0≤m≤n≤2000
.

Return: The sum of combinations C(n,k)
 for all k
 satisfying m≤k≤n
, modulo 1,000,000. In shorthand, ∑nk=m(nk)
.

Sample Dataset
6 3

Sample Output
42
"""

##  define function

def factorization(n):
    i = 2
    ret = []
    while i * i <= n:
        while n % i == 0:
            ret.append(i)
            n //= i
        i += 1
    if n > 1:
        ret.append(n)
    return ret

def subSetCount(n, k, mod=1000000):
    if n<2*k:
        k = n-k
    dataset = [i for i in range(n,n-k,-1)]
    for i in range(k,1,-1):
        tmp = factorization(i)
        for j in range(len(tmp)):
            for x in range(k):
                if not dataset[x]%tmp[j]:
                    dataset[x] /= tmp[j]
                    break
                
    total = 1
    for i in range(k):
        total *= dataset[i]
        total %=mod
    return total


##  import dataset
with open("../datasets/ASPC_dataset.txt", 'r') as f:
    n,m = map(int, f.readline().strip().split())

mod = 1000000
sum = 0

for i in range(n,m-1,-1):
    sum += subSetCount(n,i)
    sum %= mod

##  print result
print(int(sum))