##  Locating Restriction Sites
from utility import readFastaFileList

def findReversePalindrome(seq:str, short = 2, long = 6):
    dic = {'A':'T',
           'T':'A',
           'G':'C',
           'C':'G',
                 }
    
    result = []
    for p in range(short-1,len(seq)-short):
        cur, next = p, p+1
        if dic[seq[cur]] == seq[next]:
            i = 1
            while i<long:
                cur, next = cur-1, next+1
                if cur<0 or next>=len(seq):
                    break
                if dic[seq[cur]] == seq[next]:
                    i +=1
                    result.append([cur+1,i*2])
                    continue
                else:
                    break
    return result



seq = readFastaFileList("test.txt")[0]
short = 4
long = 12

for i in findReversePalindrome(seq,int(short/2), int(long/2)):
    print(f"{i[0]} {i[1]}")
