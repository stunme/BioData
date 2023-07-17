import itertools as it
import random
from collections import Counter

with open("test.txt",'r') as f:
    charListTable = [i.strip() for i in f.readlines()]

a = random.sample(charListTable,3)
x = Counter(zip(a[0],a[1],a[2]))
print(x)


for i in a:
