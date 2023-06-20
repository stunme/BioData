##  aximum Matchings and RNA Secondary Structures


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


if dic["A"]>dic["U"]:
    prob = math.factorial(dic["A"])/math.factorial(dic["A"]-dic["U"])
else:
    prob = math.factorial(dic["U"])/math.factorial(dic["U"]-dic["A"])

if dic["G"]>dic["C"]:
    prob *= math.factorial(dic["G"])/math.factorial(dic["G"]-dic["C"])
else:
    prob *= math.factorial(dic["C"])/math.factorial(dic["C"]-dic["G"])

print(prob)
