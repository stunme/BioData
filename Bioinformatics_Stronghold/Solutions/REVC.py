##	Complementing a Strand of DNA
## Skip data validation

seq = "AAAACCCGGT"

def reverseComplement(seq):
    dic = {'A':'T',
           'T':'A',
           'G':'C',
           'C':'G',
           }
    return ''.join(dic[n] for n in seq[::-1])

print(reverseComplement(seq))