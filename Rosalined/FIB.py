##Rabbits and Recurrence Relations

n,k = 32,4

def fibonacciSeq(n,k):
    parrent, total = 0, 1
    for g in range(1,n):
        # g -> generation
        parrent, total = total, total+parrent*k
    return total

print(fibonacciSeq(n,k))
