##  Edit Distance

from utility import readFastaFileList

def edit(seqI, seqJ):
    lenI, lenJ = len(seqI)+1, len(seqJ)+1
    arr = []
    arr.append([0]*lenJ)

    for i in range(1,lenI):
        arr.append([0]*lenJ)
        for j in range(1,lenJ):
            if seqI[i-1] == seqJ[j-1]:
                arr[i][j] = arr[i-1][j-1]+1
            else:
                arr[i][j] = max(arr[i][j-1],arr[i-1][j])
	
    count = 0
    cum = 0
    while i*j!=0
        if arr[i][j] == arr[i][j-1]:
            i-=1
		elif arr[i][j] == arr[i][j-1]:
		    cum -=1
		    j-=1
		else:
		    count += cum
		    cum = 0
		    i-=1
		    j-=1
    return count
    
seq = readFastaFileList("test.txt")

M = []
lenI,lenJ = len(seq[0])+1,len(seq[1])+1
for i in range(lenI):
	M.append([0]*lenJ)
for i in range(1,lenI):
	M[i][0]= i
for i in range(1,lenJ):
	M[0][i]= i

# Compute each entry of M.
for i in range(1,lenI):
	for j in range(1,lenJ):
		if seq[0][i-1] == seq[1][j-1]:
			M[i][j] = M[i-1][j-1]
		else:
			M[i][j] = min(M[i-1][j]+1,M[i][j-1]+1, M[i-1][j-1]+1)

# Print and save the desired edit distance.
print(M[lenI-1][lenJ-1])