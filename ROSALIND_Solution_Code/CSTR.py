##  Creating a Character Table from Genetic Strings 

def cstr(seqList):
    result = set()
    for i in range(len(seqList[0])):
        cur = ""
        count = 0
        head = seqList[0][i]
        for s in seqList:
            if s[i] == head:
                cur += '1'
                count += 1
            else:
                cur += '0'
        if count>len(seqList)-2 or count<2:
            continue
        result.add(cur)

    return result




with open("test.txt",'r') as f:
    seqList = [i.strip() for i in f.readlines()]

with open("result.txt",'w') as f:
    f.write('\n'.join(s for s in cstr(seqList)))
