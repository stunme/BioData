##  Constructing a De Bruijn Graph

with open("test.txt",'r') as f:
    S = set([s.strip() for s in f.readlines()])

mapping = str.maketrans("ATGC","TACG")
S |= set([s.translate(mapping)[::-1] for s in S])

with open("result.txt",'a') as f:
    for s in S:
        f.write(f"({s[:-1]}, {s[1:]})\n")