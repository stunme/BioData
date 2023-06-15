## Counting DNA Nucleotides

seq = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

def countDNA(seq):
    dic = {"A": 0,
           "C": 0,
           "G": 0,
           "T": 0,
           }
    for n in seq:
        dic[n] += 1
    return dic

print(" ".join(str(value) for key,value in countDNA(seq).items()))
