##  Enumerating Gene Orders

n = 3

import itertools as it
p = it.permutations(range(1,n+1))

for i in range(n):
    i *= (i+1)
print(i)
for i in p:
    print(" ".join(str(j) for j in i))

