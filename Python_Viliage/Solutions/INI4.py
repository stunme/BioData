##  Conditions and Loops

"""
Problem
Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.

=================================

Sample Dataset
100 200

Sample Output
7500
"""

with open("../Datasets/INI4_dataset.txt",'r') as f:
    a,b = map(int,f.readline().strip().split())

## |, e.g  2|1 = 3, 00000010 | 00000001 = 00000011  
print(sum(range(a|1,b+1,2)))

