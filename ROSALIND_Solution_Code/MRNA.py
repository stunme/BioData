##  Inferring mRNA from Protein

def mrna(seq, mod=1000000):
    dic = {
        'A':4,
        'C':2,
        'D':2,
        'E':2,
        'F':2,
        'G':4,
        'H':2,
        'I':3,
        'K':2,
        'L':6,
        'M':1,
        'N':2,
        'P':4,
        'Q':2,
        'R':6,
        'S':6,
        'T':4,
        'V':4,
        'W':1,
        'Y':2
    }
    result = 3
    for i in seq:
        result *= dic[i]
        if result > mod:
            result = result % mod
    return result


with open("test.txt",'r') as file:
    seq = file.readline().strip()
print(mrna(seq))












seq = "MA"
