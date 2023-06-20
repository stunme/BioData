##  Counting Subsets 
##  counting subset of n set is 2^n

n = 3
mod = 1000000

total = 1
for n in range(1,n+1):
    total*=2
    if total>mod:
        total %= mod

print total
