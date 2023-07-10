##  Character-Based Phylogeny 

def chbp(taxaList, charTableList):
    pass




with open("test.txt",'r') as f:
    taxaList = f.readline().strip().split()
    charTableList = [i.strip() for i in f.readlines()] 

chbp(taxaList, charTableList)