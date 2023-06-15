##  Finding a Motif in DNA

s = "GATATATGCATATACTT"
t = "ATAT"

pos = []

for i in range(len(s)-len(t)+1):
    if s[i:i+4] == t:
        pos.append(i+1)

print(' '.join(str(n) for n in pos))