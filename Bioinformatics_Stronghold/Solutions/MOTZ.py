##   Motzkin Numbers and RNA Secondary Structures


dicMatch = {'A':'U',
            'U':'A',
            'G':'C',
            'C':'G'
            }
dicAll ={}

def Motzkin(seq, mod= 1000000):
    if seq not in dicAll:
        if len(seq) < 2:
            return 1   
        sum =Motzkin(seq[1:],mod)
        for i in range(1,len(seq)):
            if dicMatch[seq[0]] == seq[i]:
                sum += Motzkin(seq[1:i],mod)*Motzkin(seq[i+1:],mod)%mod
        dicAll[seq] = sum%mod
    return dicAll[seq]


seq = readFastaFileList("test.txt")[0]

print(Motzkin(seq))



