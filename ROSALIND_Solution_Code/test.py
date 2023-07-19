i="ABCDE"
j ='abcde'

import itertools as it

for a,b in it.product(i,j):
    if a == b:
        total +