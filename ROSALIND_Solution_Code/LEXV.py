##  Ordering Strings of Varying Length Lexicographically

with open("test.txt",'r') as f:
    symbol = [i for i in f.readline().strip().split(' ')]
    n = int(f.readline())


def generate(n, seq, item=""):
    if item !="":
        seq.append(item)
    if n == 0:
        return
    for s in symbol:
        generate(n-1, seq, item+s)

seq = []
generate(n, seq)
print(len(seq))
print('\n'.join(i for i in seq))