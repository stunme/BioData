##  Enumerating Oriented Gene Orderings
##   signed permutation

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

n= 3
tmp = sign(n)

print(len(tmp))
for i in tmp:
    print(" ".join(str(j) for j in i))
