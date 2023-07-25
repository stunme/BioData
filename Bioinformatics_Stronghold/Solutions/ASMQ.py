##  Assessing Assembly Quality with N50 and N75

"""
Problem
Given a collection of DNA strings representing contigs, we use the N statistic NXX (where XX ranges from 01 to 99) to represent the maximum positive integer L
 such that the total number of nucleotides of all contigs having length ≥L
 is at least XX% of the sum of contig lengths. The most commonly used such statistic is N50, although N75 is also worth mentioning.

Given: A collection of at most 1000 DNA strings (whose combined length does not exceed 50 kbp).

Return: N50 and N75 for this collection of strings.

Sample Dataset
GATTACA
TACTACTAC
ATTGAT
GAAGA

Sample Output
7 6
"""
##  define function
def nxx(lenList,xx):
    countList = [0]*(max(lenList)+1)
    for i in lenList:
        countList[i] +=i
    nxx = sum(lenList)*(100-xx)/100
    
    for i in range(1,len(countList)):
        countList[i] += countList[i-1]
        if countList[i]>nxx:
            return i

##  import dataset
with open("../datasets/ASMQ_dataset.txt",'r') as f:
    lenList = [len(i.strip()) for i in f.readlines()]

##  print result
print(nxx(lenList,50),nxx(lenList,75))