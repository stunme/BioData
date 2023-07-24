##  Sex-Linked Inheritance

with open('test.txt') as f:
    A = map(float,f.readline().strip().split(" "))
    

B = [round(2*(x - x**2),3) for x in A]

print(' '.join(map(str,B)))
