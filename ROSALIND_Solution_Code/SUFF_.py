with open("test.txt","r") as f:
    seq = f.readline().strip()


class suffixTree(object):
    __edge = {}
    def __init__(self,seq):
        self.__sequence = seq
        self.__root = suffixNode("",1)
        self.__constructTree()

    def __constructTree(self):
        pass

    def seq(self):
        return self.__sequence

    def root(self):
        return self.__root

    
    class node(object):
        __num  = 0
        __pos  = 0
        __child = []
        def __init__ (self,parent,num):
            self.__parent = parent
            self.__num = num

        def getNumber(self):
            return self.__num

        def getParent(self):
            return self.__parent

        def changeParent(self, parent):
            self.__parent = parent

        def addChild(self, child):
            self.__child.append(child)

        def delChild(self, child):
            self.__child.remove(child)

        def iterChild(self, child):
            return i for i in self.__child


tree = suffixTree(seq)
