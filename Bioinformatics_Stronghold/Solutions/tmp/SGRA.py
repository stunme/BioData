##  Using the Spectrum Graph to Infer Peptides

##  Using the Spectrum Graph to Infer Peptides

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
with open("test.txt","r") as f:
    massList = [float(i.strip()) for i in f.readlines()]

## not sure the orginal data is sorted or not.
massList.sort(reverse = True)

aaDic = {}
treeDic = {}
#creat all potential edges
for i in range(len(massList)):
    for j in range(i+1,len(massList)):
        tmp = round(massList[i]-massList[j],2)
        if tmp in massDic:
            if j in treeDic:
                treeDic[j].append(i)
            else:
                treeDic[j] = [i]
            aaDic[(j,i)] = massDic[tmp]

# find longest peptide
def longestPeptide(start, seq):
    if start ==0 or start not in treeDic:
        return seq
    maxLen = 0
    curSeq = ""
    for i in treeDic[start]:
        tmp = longestPeptide(i,aaDic[start,i])
        if len(tmp)> maxLen:
            maxLen = len(tmp)
            curSeq = tmp
    return seq+curSeq
    
print longestPeptide(len(massList)-1,"")
