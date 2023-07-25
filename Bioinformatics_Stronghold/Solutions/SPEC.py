##  Inferring Protein from Spectrum 

"""
Problem
The prefix spectrum of a weighted string is the collection of all its prefix weights.

Given: A list L
 of n
 (n≤100
) positive real numbers.

Return: A protein string of length n−1
 whose prefix spectrum is equal to L
 (if multiple solutions exist, you may output any one of them). Consult the monoisotopic mass table.

Sample Dataset
3524.8542
3710.9335
3841.974
3970.0326
4057.0646

Sample Output
WMQS
"""

HOH = 18.01056 
dic = {
    'A':   71.03711,
    'C':  103.00919,
    'D':   115.02694,
    'E':   129.04259,
    'F':   147.06841,
    'G':   57.02146,
    'H':   137.05891,
    'I':   113.08406,
    'K':   128.09496,
    'L':   113.08406,
    'M':   131.04049,
    'N':   114.04293,
    'P':   97.05276,
    'Q':   128.05858,
    'R':   156.10111,
    'S':   87.03203,
    'T':   101.04768,
    'V':   99.06841,
    'W':   186.07931,
    'Y':   163.06333 }

massDic = {}
for k,v in dic.items():
    massDic[round(v,2)] = k

with open("../datasets/SPEC_dataset.txt","r") as f:
    massList = [float(i.strip()) for i in f.readlines()]

peptide = ""
for i in range(len(massList)-1,0,-1):
    peptide = massDic[round(massList[i]-massList[i-1],2)]+peptide

##  print result
print(peptide, len(peptide))
