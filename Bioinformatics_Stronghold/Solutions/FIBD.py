##  Mortal Fibonacci Rabbits

"""
Problem

Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2
 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100
 and m≤20
.

Return: The total number of pairs of rabbits that will remain after the n
-th month if all rabbits live for m
 months.

Sample Dataset

6 3
Sample Output
4
"""


## define function 
def fibonacciSeqMortal(n,m):
    parrent, total = 0, 1
    death = []
    for g in range(1,n):
        #g -> generation
        death.append(total-parrent)
        if g<m:
            parrent, total = total, total+parrent
        else:
            parrent, total = total-death[g-m], total+parrent-death[g-m]
        
    return total

##  input dataset
with open("../datasets/FIBD_dataset.txt",'r') as f:
    n,m = map(int,f.readline().strip().split())

##  print output
print(fibonacciSeqMortal(n,m))
