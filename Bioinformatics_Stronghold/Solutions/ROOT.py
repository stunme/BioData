##  Counting Rooted Binary Trees

"""
Problem
As in the case of unrooted trees, say that we have a fixed collection of n
 taxa labeling the leaves of a rooted binary tree T
. You may like to verify that (by extension of “Counting Phylogenetic Ancestors”) such a tree will contain n−1
 internal nodes and 2n−2
 total edges. Any edge will still encode a split of taxa; however, the two splits corresponding to the edges incident to the root of T
 will be equal. We still consider two trees to be equivalent if they have the same splits (which requires that they must also share the same duplicated split to be equal).

Let B(n)
 represent the total number of distinct rooted binary trees on n
 labeled taxa.

Given: A positive integer n
 (n≤1000
).

Return: The value of B(n)
 modulo 1,000,000.

Sample Dataset
4

Sample Output
15
"""


import functools

with open("../datasets/ROOT_dataset.txt",'r') as f:
    n = int(f.readline().strip())


# The total number of unrooted trees is just the double factorial (2n -5)!!
# Can transform an unrooted binary tree into a rooted binary tree by inserting
# a node into any of its 2*n - 3 edges.

unroot = functools.reduce(lambda a,b: a*b% 10**6, range(2*n-5,1,-2))
print(unroot*(2*n - 3) % 10**6)