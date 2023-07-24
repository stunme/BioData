##  Mortal Fibonacci Rabbits

n,m = 84,20 

def fibonacciSeqMortal(n,m):
    parrent, total = 0, 1
    death = []
    for g in range(1,n):
        #g -> generation
        death.append(total-parrent)
        if g<m:
            parrent, total = total, total+parrent
        else:
            parrent, total = total-death[g-m], total+parrent-death[g-m]
        
    return total

print(fibonacciSeqMortal(n,m))
