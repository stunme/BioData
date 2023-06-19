##  Introduction to Set Operations

n = 10
setC = set(i for i in range(1,n+1))
set1 ={1, 2, 3, 4, 5}
set2 = {2, 8, 5, 10}


print(set1|set2)
print(set1&set2)
print(set1-set2)
print(set2-set1)
print(setC-set1)
print(setC-set2)
