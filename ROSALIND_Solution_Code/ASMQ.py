##  Assessing Assembly Quality with N50 and N75

def nxx(lenList,xx):
    countList = [0]*(max(lenList)+1)
    for i in lenList:
        countList[i] +=i
    nxx = sum(lenList)*(100-xx)/100
    
    for i in range(1,len(countList)):
        countList[i] += countList[i-1]
        if countList[i]>nxx:
            return i


with open("test.txt",'r') as f:
    lenList = [len(i.strip()) for i in f.readlines()]

print(nxx(lenList,50),nxx(lenList,75))