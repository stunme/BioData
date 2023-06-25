##  Wright-Fisher's Expected Behavior

with open("test.txt","r") as f:
    n = int(f.readline().strip())
    P = map(float, f.readline().strip().split(" "))


print(" ".join(str(n*i) for i in P))
