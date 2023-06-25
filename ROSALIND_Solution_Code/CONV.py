##  Comparing Spectra with the Spectral Convolution

with open("test.txt",'r') as f:
    set1 = [float(i) for i in f.readline().strip().split()]
    set2 = [float(i) for i in f.readline().strip().split()]

dic = {}
maxDiff = 0
maxCount = 1

for i in set1:
    for j in set2:
        tmp = round(abs(i-j),5)
        if tmp in dic:
            dic[tmp] += 1
            if maxCount < dic[tmp]:
                maxCount = dic[tmp]
                maxDiff = tmp
        else:
            dic[tmp] = 1 

print(maxCount)
print(maxDiff)


##  or you can use Counter.most_common

