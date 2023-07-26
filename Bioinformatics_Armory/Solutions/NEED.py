##  Pairwise Global Alignment

"""
Problem
An online interface to EMBOSS's Needle tool for aligning DNA and RNA strings can be found here.

Use:

The DNAfull scoring matrix; note that DNAfull uses IUPAC notation for ambiguous nucleotides.
Gap opening penalty of 10.
Gap extension penalty of 1.
For our purposes, the "pair" output format will work fine; this format shows the two strings aligned at the bottom of the output file beneath some statistics about the alignment.

Given: Two GenBank IDs.

Return: The maximum global alignment score between the DNA strings associated with these IDs.

==================================================
Sample Dataset
JX205496.1 JX469991.1

Sample Output
257
"""

from urllib import parse
from urllib import request

def getFasta(accessNum):
    ## get the real id#
    with request.urlopen("https://www.ncbi.nlm.nih.gov/nuccore/"+accessNum) as r:
        page = r.read().decode('utf-8')
    a = page.find('name="ncbi_uidlist"')
    b = page[a:].find('/>')
    id = page[a:a+b].split('"')[-2]

    url = "https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?"

    param ={ 
            "db"            :   "nuccore",
            "report"        :   "fasta",
            "extrafeat"     :   "null",
            "conwithfeat"   :   "on",
            "hide-cdd"      :   "on",
            "retmode"       :   "on",
            "tool"          :   "portal",
            "log$"          :   "seqview",
            "maxdownloadsize":  "1000000",
            "id"            :   id
    }

    ##  get Fasta information
    with request.urlopen(url+parse.urlencode(param)) as r:
        label = r.readline().decode('utf-8').strip()
        seq = ''.join(s.decode('utf-8').strip() for s in r.readlines())

    return [label,seq]
    
def gaff(seq1, seq2, scoreMatrix, a, b):
   lenI, lenJ = len(seq1)+1, len(seq2)+1
   arr = []
   arrI = []
   arrJ = []
   for i in range(lenI):
      arr.append([0]*lenJ)
      arrI.append([0]*lenJ)
      arrJ.append([0]*lenJ)
   for j in range(1, lenJ):
      gap = -a-b*(j-1)
      arr[0][j] = gap
      arrI[0][j] = gap
      arrJ[0][j] = gap
   for i in range(1, lenI):
      gap = -a-b*(i-1)
      arr[i][0] = gap
      arrI[i][0] = gap
      arrJ[i][0] = gap

   for i in range(1,lenI):
      for j in range(1, lenJ):
         arr[i][j] = max(arr[i-1][j-1]+scoreMatrix[seq1[i-1]+seq2[j-1]],
                         arrJ[i][j-1]-a,
                         arrI[i-1][j]-a
                         )
         arrI[i][j] = max(arrI[i-1][j]-b,arr[i][j])
         arrJ[i][j] = max(arrJ[i][j-1]-b,arr[i][j])

   return arr[lenI-1][lenJ-1]

## parse dataset
with open("../Datasets/NEED_dataset.txt",'r') as f:
    accessNums = f.readline().strip().split()

## get two seq
fastas = [getFasta(n)[1] for n in accessNums] 

## construct DNAfull scoring dict
with open("../utility/DNAfull.txt","r") as f:
    nt = f.readline().strip().split()
    m = [l.strip().split() for l in f.readlines()]
scoreMatrix = {}
for i in range(len(nt)):
   for j in range(1,len(nt)+1):
      scoreMatrix[nt[i]+nt[j-1]] = int(m[i][j])

a,b =10,1

## use GAFF.py
print(gaff(fastas[0],fastas[1],scoreMatrix,a,b))
