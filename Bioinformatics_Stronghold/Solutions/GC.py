##  Computing GC Content
##  skip data validation

from utility import readFastaFileDict
from DNA import countDNA

seqDic = readFastaFileDict("test.txt")

dic = {}

for key, value in seqDic.items():
    tmp = countDNA(value)
    dic[key] = (tmp['G']+tmp['C'])/len(value)*100

id = max(dic,key = dic.get)
print(f"{id}\n{dic[id]}")
