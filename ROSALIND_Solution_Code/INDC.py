##  Independent Segregation of Chromosomes

import math

n = 49

N = 2*n

prob = 0.5

tmp = [0]

for k in range(N,1,-1):
    tmp.append(prob**N*math.factorial(N)/math.factorial(k)/math.factorial(N-k)+tmp[N-k])

tmp.append(1)

B = [round(math.log10(i),3) for i in tmp[-1:0:-1]]

print(" ".join(str(i) for i in B))