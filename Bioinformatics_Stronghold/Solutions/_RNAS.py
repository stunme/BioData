##  Wobble Bonding and RNA Secondary Structures

dicAll ={}

def rnas(seq):
    if seq not in dicAll:
        if len(seq) < 5:
            return 1   
        sum =rnas(seq[1:])
        for i in range(4,len(seq)):
            if seq[0]+seq[i] in ["AU","UA","GU","UG","GC","CG"]:
                sum += rnas(seq[1:i])*rnas(seq[i+1:])
        dicAll[seq] = sum
    return dicAll[seq]


with open("test.txt","r") as f:
  seq = f.readline().strip()

print(rnas(seq))



