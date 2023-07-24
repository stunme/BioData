##  Matching a Spectrum to a Protein

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

with open("test.txt",'r') as f:
    n = int(f.readline().strip())
    seqList = []
    specList = []
    for i in range(n):
        tmp = f.readline().strip()
        mass = 0
        specList.append([])
        for j in tmp:
            mass += dic[j]
            specList[-1].append(round(mass,5))
        full = specList[-1][-1]
        for j in range(len(specList[-1])-1):
            # print(j)
            specList[-1].append(round(full - specList[-1][j],5))
        seqList.append (tmp)
    massList = [round(float(i.strip()),5) for i in f.readlines()]

from collections import Counter

maxSeq = ""
maxCount = 0
for i in range(len(specList)):
    count = Counter([round(abs(s-t),5) for s in massList for t in specList[i]]).most_common(1)
    if maxCount<count[0][1]:
        maxCount = count[0][1]
        maxSeq = seqList[i]

print(maxCount)
print(maxSeq)






