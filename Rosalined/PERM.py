##  Enumerating Gene Orders

n = 3

def enumer(n):
    res = [""]
    for k in range(n):
        tmp = []
        for i in res:
            for j in range(1,n+1):
                if not str(j) in i:
                    tmp.append(i+str(j))
        res = tmp

    return res

tmp = enumer(n)
print(len(tmp))
for i in tmp:
    print(" ".join(k for k in i))