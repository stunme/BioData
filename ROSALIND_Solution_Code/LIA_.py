##  Independent Alleles

n, k = 1, 1

def LIA(n, k):
    result = {  
        "AA":0,
        "Aa":1,
        "aa":0
    } 
    proDic = {
        "AAAA":0.5,
        "AAAa":0.5,
        "AAaa":0,
        "AaAA":0.25,
        "AaAa":0.5,
        "Aaaa":0.25,
        "aaAA":0,
        "aaAa":0.5,
        "aaaa":0.5
    }
    #probability of {genotype} in offsprint by mating with Aa
    parrent = 1
    parrentDic = result
    for i in range(n):
        parrent *= 2
        
        childDic = {
            "AA":0,
            "Aa":0,
            "aa":0
        }
        for pk,pv in parrentDic.items():
            for ck,cv in childDic.items():
                childDic[ck] = cv + proDic[pk+ck]*pv
        
        for key in parrentDic:
            parrentDic[key] = childDic[key]

    return childDic


n, k = 10, 1
for k,v in LIA(n,k).items():
    print(f"{k}->{v}")