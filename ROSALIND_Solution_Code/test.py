import itertools as it
taxas = "ABCDEF"

set1 = "1234567899128391748772783560891740921473312356"

checker = set()
for i in range(1,len(taxas)):
    for x in it.combinations(taxas[1:],i):
        tmp1 = [m for m in taxas if m not in x]
        for j in range(1,len(tmp1)):
            for y in it.combinations(tmp1[1:],j):
                tmp2 = tuple([m for m in tmp1 if m not in y])
                ct = [""]*6
                for m in range(len(taxas)):
                    if taxas[m] in tmp2:
                        ct[0] += "1"
                        ct[1] += "0"
                    else:
                        ct[0] += "0"
                        ct[1] += "1"
                for m in range(len(taxas)):
                    if taxas[m] in y:
                        ct[2] += "1"
                        ct[3] += "0"
                    else:
                        ct[2] += "0"
                        ct[3] += "1"
                for m in range(len(taxas)):
                    if taxas[m] in x:
                        ct[4] += "1"
                        ct[5] += "0"
                    else:
                        ct[4] += "0"
                        ct[5] += "1"
                noFind = True
                for m in ct:
                    if m.count("0")<2 or m.count("1")<2:
                        continue
                    elif m in checker:
                        noFind = False
                        break
                if noFind:
                    for m in ct:
                        checker.add(m)
                    print(x,tmp2,y)
                        # print(tmp2,xy,xt,yt,"===========")

    count = 0
    for a,b in it.combinations(sl[-2:],2):
        for x,y in zip(a,b):
            if x!=y:
                count -= 1
    print(count)