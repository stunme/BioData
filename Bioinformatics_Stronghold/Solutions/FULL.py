##  Inferring Peptide from Full Spectrum

"""
Problem
Say that we have a string s
 containing t
 as an internal substring, so that there exist nonempty substrings s1
 and s2
 of s
 such that s
 can be written as s1ts2
. A t-prefix contains all of s1
 and none of s2
; likewise, a t-suffix contains all of s2
 and none of s1
.

Given: A list L
 containing 2n+3
 positive real numbers (n≤100
). The first number in L
 is the parent mass of a peptide P
, and all other numbers represent the masses of some b-ions and y-ions of P
 (in no particular order). You may assume that if the mass of a b-ion is present, then so is that of its complementary y-ion, and vice-versa.

Return: A protein string t
 of length n
 for which there exist two positive real numbers w1
 and w2
 such that for every prefix p
 and suffix s
 of t
, each of w(p)+w1
 and w(s)+w2
 is equal to an element of L
. (In other words, there exists a protein string whose t
-prefix and t
-suffix weights correspond to the non-parent mass values of L
.) If multiple solutions exist, you may output any one.

Sample Dataset
1988.21104821
610.391039105
738.485999105
766.492149105
863.544909105
867.528589105
992.587499105
995.623549105
1120.6824591
1124.6661391
1221.7188991
1249.7250491
1377.8200091

Sample Output
KEKEP
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
## creat a dict for index amino acid by mass
massDic = {}
for k,v in dic.items():
    massDic[round(v,2)] = k

## read the input file
with open("../datasets/FULL_dataset.txt","r") as f:
    massList = [float(i.strip()) for i in f.readlines()]

## not sure the orginal data is sorted or not. Make a reverse sort for al data
massList.sort(reverse = True)

## set the max mass substring as starting point 
cur = 1
peptide = ""

while len(massList)>3:
    for i in range(cur+1,len(massList)):
        tmp = round(massList[cur]-massList[i],2)
        ## substact the cur mass to all other smaller substring mass
        ## add the amino acid to peptide, rand remove b-ion and y-ion
        ## reset the cur 
        if tmp in massDic:
            peptide += massDic[tmp]
            right = len(massList)-cur
            del massList[cur]
            if right > cur:
                del massList[-cur]
            else:
                del massList[right]
            if right >i:
                cur = i-1
            else:
                cur = i-2
            break

  
print(peptide)
