##  Creating a Character Table

import re
def ctbl(treeStr):
    tokens = re.split('([(),])',treeStr)
    charTable = [['1']]
    stack = [[1]]
    curLeft = 1
    # newTwoPos = 1

    for t in tokens:
        if t == '(':
            stack += [[curLeft]]
        elif t not in ',()':
            stack[-1].append(t)
        elif t == ')':
            cur = stack.pop()
            left,cur = cur[0], cur[1:]
            for i in range(len(cur)):
                charTable += [['0']*len(charTable[-1])]
                charTable[-1][0] = cur[i]
            curLeft += len(cur)
            for i in range(left):
                charTable[i].append('0')
            for i in range(left,curLeft):
                charTable[i].append('1')
    print(charTable)            

        # if t == '(':
        #     stack += [[newTwoPos]]
        # elif t not in ',()':
        #     stack[-1].append(t)
        # elif t == ')':
        #     cur = stack.pop()
        #     print(cur[0],newTwoPos)
            
        #     if cur[0]+1 < len(charTable) and stack != [[1]] and cur[0]+2 !=newTwoPos and cur[0]!=newTwoPos:
        #         for i in range(cur[0]):
        #                 charTable[i].append('0')
        #         for i in range(cur[0],len(charTable)):
        #             charTable[i].append('1')

        #     if len(cur)<2:
        #         continue
        #     elif len(cur)>2:
        #         for i in charTable:
        #             i.append('0')
        #         for i in range(1,len(cur)):
        #             charTable += [['0']*len(charTable[-1])]
        #             charTable[-1][0] = cur[i]
        #             charTable[-1][-1] = '1'
        #         newTwoPos = len(charTable)
        #     else:    
        #         for i in range(1,len(cur)):
        #             charTable += [['0']*len(charTable[-1])]
        #             charTable[-1][0] = cur[i]
        #         for i in range(cur[0]):
        #             charTable[i].append('0')
        #         for i in range(cur[0],len(charTable)):
        #             charTable[i].append('1')
                
        # print(charTable)
            
    
    # print(num,num0,num2)
    charTable.sort()
    for i in charTable:
        i.pop()
    return charTable[1:]

with open("test.txt",'r') as f:
    treeStr = f.readline().strip().replace(";",'')

ctbl_ = ctbl(treeStr)

with open("result.txt",'w') as f:
    for i in range(1,len(ctbl_[0])):
        f.write(" ".join((j[i]) for j in ctbl_))
        f.write("\n")



with open("result.txt","r") as f:
   a, b= [],[]
   for l in f.readlines():
      a.append(l.strip())
      b.append(l.strip().replace('1','7').replace('0','1').replace('7','0'))


for x in range(len(a)-1,-1,-1):
   for y in range(len(b)-1,x-1,-1):
      if a[x] == b[y]:
        print(len(a), len(b), y+1)
print(len(a),len(a[0]))
