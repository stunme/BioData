##  Introduction to Alternative Splicing 


def factorization(n):
    i = 2
    ret = []
    while i * i <= n:
        while n % i == 0:
            ret.append(i)
            n //= i
        i += 1
    if n > 1:
        ret.append(n)
    return ret

def subSetCount(n, k, mod=1000000):
    if n<2*k:
        k = n-k
    dataset = [i for i in range(n,n-k,-1)]
    for i in range(k,1,-1):
        tmp = factorization(i)
        for j in range(len(tmp)):
            for x in range(k):
                if not dataset[x]%tmp[j]:
                    dataset[x] /= tmp[j]
                    break
                
    total = 1
    for i in range(k):
        total *= dataset[i]
        total %=mod
    return total





n,m =1635, 1069

mod = 1000000

sum = 0


for i in range(n,m-1,-1):
    sum += subSetCount(n,i)
    sum %= mod

print(sum)