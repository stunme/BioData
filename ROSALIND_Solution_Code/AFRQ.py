##  Counting Disease Carriers

import math

with open('test.txt') as f:
    A = map(float,f.readline().strip().split(" "))
    

B = [round(2*math.sqrt(i)-i,3) for i in A]

print(' '.join(map(str,B)))

