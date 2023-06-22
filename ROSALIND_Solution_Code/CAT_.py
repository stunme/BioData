##  Catalan Numbers and RNA Secondary Structures

def validatePerfect(seq):
    if not len(seq)%2:
        dic = {"A":0,
               "U":0,
               "G":0,
               "C":0
               }
        for i in seq:
            dic[i] += 1
        if dic["A"] == dic["U"] and dic["G"] == dic["C"]:
            return False
    return True

def catalan(seq, mod = 1000000):
    
    if validatePerfect(seq):
        return 0
    if len(seq)==2:
        return 1
    sum = catalan(seq[1:-1])%mod+catalan(seq[2:])%mod
    for i in range(3,len(seq)-1,2):
        sum += (catalan(seq[1:i-1])*catalan(seq[i+1:]))%mod
    return sum%mod

seq = "UAGCGUGAUCAC"
print catalan(seq)
