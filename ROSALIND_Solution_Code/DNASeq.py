class DNASeq(object):
    __sequence = ""
    __nucleotide = ['A', 'C', 'G', 'T']
    __DNACompliment = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
    __label = ""
    __DNACodons = {
    # 'M' - START, '_' - STOP
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TGT": "C", "TGC": "C",
    "GAT": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "TTT": "F", "TTC": "F",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAT": "H", "CAC": "H",
    "ATA": "I", "ATT": "I", "ATC": "I",
    "AAA": "K", "AAG": "K",
    "TTA": "L", "TTG": "L", "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATG": "M",
    "AAT": "N", "AAC": "N",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S", "AGT": "S", "AGC": "S",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TGG": "W",
    "TAT": "Y", "TAC": "Y",
    "TAA": "_", "TAG": "_", "TGA": "_"
    }

    __RNACodons = {
    # 'M' - START, '_' - STOP
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H",
    "AUA": "I", "AUU": "I", "AUC": "I",
    "AAA": "K", "AAG": "K",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUG": "M",
    "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAA": "_", "UAG": "_", "UGA": "_"
    }


    def __init__(self, seq, label = ""):
        if isinstance(seq,int):
            import random
            self.__sequence = ''.join([random.choice(self.__nucleotide) for i in range(seq)])
        else:
            self.__sequence = self.validateDNA(seq)
            assert self.__sequence != "", f"The seqence is not validate DNA sequence"
        self.__label = label

    def validateDNA(self, seq):
        tmpSeq = seq.upper()
        for n in tmpSeq:
            if n not in self.__nucleotide:
                return ""
            return tmpSeq
        
    def getLabel(self):
        return self.__label

    def getSeq(self):
        """return whole sequence by 5'->3'"""
        return self.__sequence
    
    def countBase(self):
        tmpDic = {'A':0, 'C':0, 'G':0, 'T':0}
        for nu in self.__sequence:
            tmpDic[nu] += 1
        return tmpDic
    
    def length(self):
        return len(self.__sequence)
    
    def complement(self):
        """return reverse complement sequencing 3'->5'"""
        return ''.join([self.__DNACompliment[nu] for nu in self.__sequence])
    
    def reverseComplement(self):
        """return reverse complement sequencing 5'->3'"""
        return ''.join([self.__DNACompliment[nu] for nu in self.__sequence[::-1]])
        # mapping = str.maketrans("ATGC","TACG")
        # return self.__sequence.translate(mapping)[::-1]
    
    def transcript(self):
        """transcript DNA->RNA by replacing T by U"""
        return self.__sequence.replace('T','U')
    
    def GCContent(self):
        tmpDic = self.countBase()
        return round((tmpDic['G']+tmpDic['C'])/self.length()*100,6)

    def addSeq(self, seq):
        return DNASeq(self.__sequence + seq)
            
    def translate(self, initPos = 0, seq = 'Y'):
        if seq == 'Y':
            seq = self.__sequence
        return ''.join([self.__DNACodons[seq[pos:pos+3]] for pos in range(initPos,len(seq)-2,3)])
    
    def translateRNA(self, initPos = 0, seq = 'Y'):
        if seq == 'Y':
            seq = self.__sequence
        return ''.join([self.__RNACodons[seq[pos:pos+3]] for pos in range(initPos,len(seq)-2,3)])
    
    def condonFrequence(self, AALetter, initPos = 0):
        tmpCodon = [self.__sequence[pos:pos+3] for pos in range(initPos,self.length()-2,3) if self.__DNACodons[self.__sequence[pos:pos+3]] == AALetter]
        resultDic = {key:0 for key, value in self.__DNACodons.items() if value == AALetter}
        for c in tmpCodon:
            resultDic[c] +=1
        return {key:round(value/len(tmpCodon),2) for key, value in resultDic.items()}
    
    def findOpenFrame(self):
        frame = {}
        frame['Foward_0'] = self.translate(0)
        frame['Foward_1'] = self.translate(1)
        frame['Foward_2'] = self.translate(2)
        rcseq=self.reverseComplement()
        frame['Backward_0'] = self.translate(0, rcseq)
        frame['Backward_1'] = self.translate(1, rcseq)
        frame['Backward_2'] = self.translate(2, rcseq)
        return frame

    def findProteins(self, aaSeq):
        proteins = []
        end, start = 0,0
        for i in range(len(aaSeq)-1,0,-1):
            if aaSeq[i] == '_':
                end = i
            elif aaSeq[i]=='M' and end > 0:
                proteins.append(aaSeq[i:end])
        return [seq for seq in proteins[::-1]]
    

    def findAllProteins(self, ordered = False):
        orfs = set()

        for key, aa in self.findOpenFrame().items():
            for pro in self.findProteins(aa):
                orfs.add(pro)
 
        if ordered:
            return sorted(list(orfs), key = len, reverse = True)
        return list(orfs)
