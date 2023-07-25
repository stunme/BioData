##  Counting Unrooted Binary Trees

import functools

n = 1000
#   The total number is just the double factorial (2n-5), e.g  n = 7, then it is 9*7*5*3*1
print(functools.reduce(lambda a, b: a*b % 10**6, range(2*n-5, 1, -2)))

