##  Independent Alleles

import math

proY = 0.25
proN = 1-proY
# aa
k, N = 2, 1                                                                        
P = 2**k                                                                       
probability = 0
# at least N, sum all N values between (N,P)
for i in range(N, P + 1):                                                      
    prob = (math.factorial(P) /                      
            (math.factorial(i) * math.factorial(P - i))) * (proY**i) * (proN**(P - i))                                                        
    probability += prob                                                        

print(round(probability,3))           
