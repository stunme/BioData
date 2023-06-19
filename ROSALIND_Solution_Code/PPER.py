##  Partial Permutations

def pper(n, k, mod = 1000000):
    result = 1
    for i in range(n,n-k,-1):
        result *=i
        if result > mod:
            result %= mod
    return result


n, k = 93, 9
print(pper(n,k))
