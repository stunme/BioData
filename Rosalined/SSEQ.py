##  Finding a Spliced Motif
##  Skip data validation

from utility import readFastaFileList

def splicedMotif(seq, motif):
    result = []
    cur = 0
    for n in motif:
        cur += seq[cur:].find(n)+1
        result.append(cur)
    return result

dataset = readFastaFileList("test.txt")
print(" ".join(str(i) for i in splicedMotif(dataset[0],dataset[1])))
    
