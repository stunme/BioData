##  Counting Point Mutations
##  skip data validation

seq1="GAGCCTACTAACGGGAT"
seq2="CATCGTAATGACGGCCT"

def countMutations(seq1, seq2):
    count = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            count +=1 
    return count

print(countMutations(seq1,seq2))
        