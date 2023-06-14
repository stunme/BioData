##  Transitions and Transversions
##  Skip data validation

from utility import readFastaFileList

def TnT(seqList):
    dic = {'A':'G',
           'G':'A',
           'T':'C',
           'C':'T',
    }
    transitions, transversions = 0,0

    for i in range(len(seqList[0])):
        if seqList[0][i] == seqList[1][i]:
            continue
        elif dic[seqList[0][i]] == seqList[1][i]:
            transitions += 1
        else:
            transversions += 1
    return transitions/transversions

print(TnT(readFastaFileList("test.txt")))