##  Reversal Distance

def distance(seqTarget,seq):
    n = len(seq)
    result = 0
    dummy = [i for i in seq]
    for i in range(n):
        if seqTarget[i] != dummy[i]:
            result +=1
            tmp = []
            for j in range(i,n):
                tmp.append(dummy[j])
                if seqTarget[i] == dummy[j]:
                    for k in range(1,len(tmp)+1):
                        dummy[i+k-1] = tmp[-k]
                    print(dummy)
                    break
    return result


dataset = []
with open("test.txt","r") as f:
    for i in f.readlines():
        tmp = i.strip().split(" ")
        if len(tmp)>1:
            dataset.append(tmp)

print(distance(dataset[4],dataset[5]))

#print(" ".join(str(distance(dataset[i],dataset[i+1])) for i in range(0,len(dataset),2)))
    
    