##  Introduction to Set Operations

with open("test.txt","r") as f:
    n = int(f.readline().strip())
    setC = set(i for i in range(1,n+1))
    set1 = set(int(i) for i in f.readline().strip().strip(" {}").split(","))
    set2 = set(int(i) for i in f.readline().strip().strip(" {}").split(","))


print(set1|set2)
print(set1&set2)
print(set1-set2)
print(set2-set1)
print(setC-set1)
print(setC-set2)
