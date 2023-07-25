##  Wright-Fisher's Expected Behavior

"""
Problem
In “The Wright-Fisher Model of Genetic Drift”, we generalized the concept of a binomial random variable Bin(n,p)
 as a "weighted coin flip." It is only natural to calculate the expected value of such a random variable.

For example, in the case of unweighted coin flips (i.e., p=1/2
), our intuition would indicate that E(Bin(n,1/2))
 is n/2
; what should be the expected value of a binomial random variable?

Given: A positive integer n
 (n≤1000000
) followed by an array P
 of length m
 (m≤20
) containing numbers between 0
 and 1
. Each element of P
 can be seen as representing a probability corresponding to an allele frequency.

Return: An array B
 of length m
 for which B[k]
 is the expected value of Bin(n,P[k])
; in terms of Wright-Fisher, it represents the expected allele frequency of the next generation.

Sample Dataset
17
0.1 0.2 0.3

Sample Output
1.7 3.4 5.1
"""


with open("../datasets/EBIN_dataset.txt","r") as f:
    n = int(f.readline().strip())
    P = map(float, f.readline().strip().split(" "))


print(" ".join(str(n*i) for i in P))
