### RNA Splicing
from utility import readFastaFileList
from DNASeq import DNASeq

seq = readFastaFileList("testdata/test.txt")
cDNA = seq[0]
for s in seq[1:]:
    cDNA = cDNA.replace(s,'')

print(DNASeq(cDNA).findOpenFrame()['Foward_0'])



