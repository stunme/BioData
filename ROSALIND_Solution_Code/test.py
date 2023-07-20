# from EDIT import edit

# with open("test.txt",'r') as f:
#     k = int(f.readline().strip())
#     motif = f.readline().strip()
#     genome = f.readline().strip()

# with open("result.txt",'r') as f:
#     pair = [i.strip().split() for i in f.readlines()]


# for i,j in pair:
#     with open("result_1.txt",'a') as f:
#         f.write(f"{i}--{j}---->{str(edit(motif,genome[int(i)-1:int(i)-1+int(j)]))}\n")


import time

myList = [i for i in range(1000000)]

start = time.time()
for i in myList:
    a = {i}
print(time.time()-start)