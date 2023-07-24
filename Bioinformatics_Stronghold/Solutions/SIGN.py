##  Enumerating Oriented Gene Orderings
##   signed permutation

"""
Problem
A signed permutation of length n
 is some ordering of the positive integers {1,2,…,n}
 in which each integer is then provided with either a positive or negative sign (for the sake of simplicity, we omit the positive sign). For example, π=(5,−3,−2,1,4)
 is a signed permutation of length 5
.

Given: A positive integer n≤6
.

Return: The total number of signed permutations of length n
, followed by a list of all such permutations (you may list the signed permutations in any order).

Sample Dataset
2

Sample Output
8
-1 -2
-1 2
1 -2
1 2
-2 -1
-2 1
2 -1
2 1
"""

##  define funciton
import itertools as it

def sign(n):
    permutation = [i for i in it.permutations(range(1,n+1))]
    product = [i for i in it.product([-1,1],repeat=n)]
    result = []
    for i in permutation:
        for j in product:
            result.append([i[k]*j[k]for k in range(n)])
    ## may use numpy for array multiply
    return result

##  import dataset
with open("../datasets/SIGN_dataset.txt",'r') as f:
    n = int(f.readline().strip())

tmp = sign(n)

##  print output
print(len(tmp))
for i in tmp:
    print(" ".join(str(j) for j in i))
