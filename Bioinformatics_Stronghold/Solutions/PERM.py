##  Enumerating Gene Orders

"""
Problem
A permutation of length n
 is an ordering of the positive integers {1,2,…,n}
. For example, π=(5,3,2,1,4)
 is a permutation of length 5
.

Given: A positive integer n≤7
.

Return: The total number of permutations of length n
, followed by a list of all such permutations (in any order).

Sample Dataset
3

Sample Output
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""

##  input dataset
with open("../datasets/PERM_dataset.txt",'r') as f:
    n = int(f.readline().strip())

##  process data
import itertools as it
p = it.permutations(range(1,n+1))

for i in range(n):
    i *= (i+1)

##  print output    
print(i)
for i in p:
    print(" ".join(str(j) for j in i))

