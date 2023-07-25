##  Counting Rooted Binary Trees

import functools

n = 981


# The total number of unrooted trees is just the double factorial (2n -5)!!
# Can transform an unrooted binary tree into a rooted binary tree by inserting
# a node into any of its 2*n - 3 edges.

unroot = functools.reduce(lambda a,b: a*b% 10**6, range(2*n-5,1,-2))
print(unroot*(2*n - 3) % 10**6)