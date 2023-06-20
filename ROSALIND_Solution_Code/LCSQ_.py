##  Finding a Shared Spliced Motif

from utility import readFastaFileList

seq = readFastaFileList("test.txt")


matrix = []
for i in range(len(seq[0])):
    matrix.append([])
    for j in range(len(seq[1])):
        if seq[0][i] == seq[1][j]:
            matrix[i].append(1)
        else:
            matrix[i].append(0)


for i in matrix:
    print(' '.join(str(j) for j in i))