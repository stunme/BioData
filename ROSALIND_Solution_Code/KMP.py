##  Speeding Up Motif Finding 

from utility import readFastaFileList

def kmp(seq):
    P = [0]*len(seq)
    j = [0]
    for i in range(1,len(seq)):
        k = 0
        while k<len(j):
            if seq[i] == seq[j[k]]:
                j[k] += 1
            elif j[k]>0:
                del j[k]
                k-=1
            k +=1
        #print(j)
        if seq[i] == seq[0]:
            j.append(0)
        P[i] = j[0]    
    return P
a = kmp(readFastaFileList("test.txt")[0])
print(" ".join(str(i) for i in a))


def kmp1(s):
    failure_array = [0] * len(s)
    longest_motif_length = 0 # 记录最长的motif的长度，如果断了，则停止循环
    for i in range(1, len(s)):
        #print(i)
        for j in range(1, len(s)-i+1):
            if s[:i] == s[j:j+i]:
                failure_array[j+i-1] = len(s[:i])
                longest_motif_length = len(s[:i])
            # print(i, j)

        # 当前循环结束后，longest_motif_length，没有增加，则停止循环。
        if longest_motif_length < len(s[:i]):
            break
    return failure_array
    

b = kmp1(readFastaFileList("test.txt")[0])
print(" ".join(str(i) for i in b))


def kmp2(string):
    """ Calculate the Knuth-Morris-Pratt failure array
    :param string: the input string
    :return: failure array (list)
    """
    n = len(string)
    arr = [0] * n
    for i in range(1, n):
        j = arr[i - 1]
        while j > 0 and string[i] != string[j]:
            j = arr[j - 1]
        if string[i] == string[j]:
            j += 1
        arr[i] = j
    return arr

c=kmp2(readFastaFileList("test.txt")[0])

for i in range(len(a)):
    if a[i]!=b[i] or a[i]!=c[i]:
        print(i,a[i],b[i],c[i])

print(len(readFastaFileList("test.txt")[0]), len(a),len(b),len(c))

