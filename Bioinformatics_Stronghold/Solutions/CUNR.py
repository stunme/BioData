##  Counting Unrooted Binary Trees
#   The total number is just the double factorial (2n-5), e.g  n = 7, then it is 9*7*5*3*1


"""
Problem
Two unrooted binary trees T1
 and T2
 having the same n
 labeled leaves are considered to be equivalent if there is some assignment of labels to the internal nodes of T1
 and T2
 so that the adjacency lists of the two trees coincide. As a result, note that T1
 and T2
 must have the same splits; conversely, if the two trees do not have the same splits, then they are considered distinct.

Let b(n)
 denote the total number of distinct unrooted binary trees having n
 labeled leaves.

Given: A positive integer n
 (n≤1000
).

Return: The value of b(n)
 modulo 1,000,000.

Sample Dataset
5

Sample Output
15
"""

import functools

with open("../datasets/CUNR_dataset.txt",'r') as f:
    n = int(f.readline().strip())

#   The total number is just the double factorial (2n-5), e.g  n = 7, then it is 9*7*5*3*1
print(functools.reduce(lambda a, b: a*b % 10**6, range(2*n-5, 1, -2)))

