from utility import readFastaFileList

def edit(seqI,seqJ):
    lenI, lenJ = len(seqI)+1, len(seqJ)+1
    arr = []
    for i in range(lenI):
        arr.append([0]*lenJ)
    for i in range(1,lenI):
        arr[i][0] = i
    for j in range(1,lenJ):
        arr[0][j] = j

    for i in range(1,lenI):
        for j in range(1, lenJ):
            if seqI[i-1] == seqJ[j-1]:
                # arr[i][j] = min(arr[i-1][j-1],arr[i][j-1]+1,arr[i-1][j]+1)
                arr[i][j] = arr[i-1][j-1]
            else:
                arr[i][j] = min(arr[i-1][j-1],arr[i][j-1],arr[i-1][j])+1


    return arr[i][j]


with open("test.txt",'r') as f:
    k = int(f.readline().strip())
    motif = f.readline().strip()
    genome = f.readline().strip()

i = 15067
j = 4047
print(edit(motif,genome[i-1:i-1+j]))
print(edit(motif,genome[i:i-1+j]))
print(edit(motif,genome[i+1:i-1+j]))
print(edit(motif,genome[i-2:i-1+j]))


