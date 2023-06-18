##  Enumerating k-mers Lexicographically

import itertools as it

with open("test.txt",'r') as f:
        symbol = [i for i in f.readline().strip().split(" ")]
        num = int(f.readline().strip())

for i in it.product(symbol,repeat=num):
    print(''.join(i))
        
