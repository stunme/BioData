import time
k = 10
cur = [j for j in range(10000)]
start = time.time()
for i in range(1000):
    pre = cur
    cur = [0]*10000
    # pre = cur.copy()
    
print(time.time()-start)