from collections import Counter
dictA = Counter({1:3,2:5})
dictB = Counter({1:2,2:5})

print(dictA[2],(dictA-dictB)[2])