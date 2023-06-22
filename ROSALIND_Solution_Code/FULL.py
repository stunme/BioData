##  Inferring Protein from Spectrum 

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

  
print peptide
