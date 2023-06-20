##Perfect Matchings and RNA Secondary Structures

from utility import readFastaFileList
import math

seq = readFastaFileList("testdata/test.txt")[0]
    
dic = {"A":0,
       "U":0,
       "G":0,
       "C":0,
    }

for i in seq:
    dic[i] += 1

print(math.factorial(dic["A"])*math.factorial(dic["G"]))
