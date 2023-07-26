##  Data Formats  

"""
Problem
GenBank can be accessed here. A detailed description of the GenBank format can be found here. A tool, from the SMS 2 package, for converting GenBank to FASTA can be found here.

Given: A collection of b (n≤10) GenBank entry IDs.

Return: The shortest of the strings associated with the IDs in FASTA format.

Sample Dataset
FJ817486 JX069768 JX469983
Sample Output
>JX469983.1 Zea mays subsp. mays clone UT3343 G2-like transcription factor mRNA, partial cds
ATGATGTATCATGCGAAGAATTTTTCTGTGCCCTTTGCTCCGCAGAGGGCACAGGATAATGAGCATGCAA
GTAATATTGGAGGTATTGGTGGACCCAACATAAGCAACCCTGCTAATCCTGTAGGAAGTGGGAAACAACG
GCTACGGTGGACATCGGATCTTCATAATCGCTTTGTGGATGCCATCGCCCAGCTTGGTGGACCAGACAGA
GCTACACCTAAAGGGGTTCTCACTGTGATGGGTGTACCAGGGATCACAATTTATCATGTGAAGAGCCATC
TGCAGAAGTATCGCCTTGCAAAGTATATACCCGACTCTCCTGCTGAAGGTTCCAAGGACGAAAAGAAAGA
TTCGAGTGATTCCCTCTCGAACACGGATTCGGCACCAGGATTGCAAATCAATGAGGCACTAAAGATGCAA
ATGGAGGTTCAGAAGCGACTACATGAGCAACTCGAGGTTCAAAGACAACTGCAACTAAGAATTGAAGCAC
AAGGAAGATACTTGCAGATGATCATTGAGGAGCAACAAAAGCTTGGTGGATCAATTAAGGCTTCTGAGGA
TCAGAAGCTTTCTGATTCACCTCCAAGCTTAGATGACTACCCAGAGAGCATGCAACCTTCTCCCAAGAAA
CCAAGGATAGACGCATTATCACCAGATTCAGAGCGCGATACAACACAACCTGAATTCGAATCCCATTTGA
TCGGTCCGTGGGATCACGGCATTGCATTCCCAGTGGAGGAGTTCAAAGCAGGCCCTGCTATGAGCAAGTC
A
"""

## use just urllib

from urllib import parse
from urllib import request

def getFasta(accessNum):
    ## get the real id#
    with request.urlopen("https://www.ncbi.nlm.nih.gov/nuccore/"+accessNum) as r:
        page = r.read().decode('utf-8')
    a = page.find('name="ncbi_uidlist"')
    b = page[a:].find('/>')
    id = page[a:a+b].split('"')[-2]

    url = "https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?"

    param ={ 
            "db"            :   "nuccore",
            "report"        :   "fasta",
            "extrafeat"     :   "null",
            "conwithfeat"   :   "on",
            "hide-cdd"      :   "on",
            "retmode"       :   "on",
            "tool"          :   "portal",
            "log$"          :   "seqview",
            "maxdownloadsize":  "1000000",
            "id"            :   id
    }

    ##  get Fasta information
    with request.urlopen(url+parse.urlencode(param)) as r:
        label = r.readline().decode('utf-8').strip()
        seq = ''.join(s.decode('utf-8').strip() for s in r.readlines())

    return [label,seq]
    
## parse dataset
with open("../Datasets/FRMT_dataset.txt",'r') as f:
    accessNums = f.readline().strip().split()
    
## get all seq and print the shortest one

fastas = [getFasta(n) for n in accessNums]   

print('\n'.join(min(fastas,key=lambda a:len(a[1]))))


##=================================================================
"""
Here we can again use the Bio.Entrez module introduced in “GenBank Introduction”. To search for particular access IDs, you can use the function Bio.Entrez.efetch(db, rettype), which takes two parameters: the db parameter takes the database to search, and the rettype parameter takes the data format to be returned. For example, we use "nucleotide" (or "nuccore") as the db parameter for Genbank and "fasta" as the rettype parameter for FASTA format.

The following code illustrates efetch() in action. It obtains plain text records in FASTA format from NCBI's [Nucleotide] database.

# from Bio import Entrez
# Entrez.email = "your_name@your_mail_server.com"
# handle = Entrez.efetch(db="nucleotide", id=["FJ817486, JX069768, JX469983"], rettype="fasta")
# records = handle.read()
# print records
To work with FASTA format, we can use the Bio.SeqIO module, which provides an interface to input and output methods for different file formats. One of its main functions is Bio.SeqIO.parse(), which takes a handle and format name as parameters and returns entries as SeqRecords.

# from Bio import Entrez
# from Bio import SeqIO
# Entrez.email = "your_name@your_mail_server.com"
# handle = Entrez.efetch(db="nucleotide", id=["FJ817486, JX069768, JX469983"], rettype="fasta")
# records = list (SeqIO.parse(handle, "fasta")) #we get the list of SeqIO objects in FASTA format
# print records[0].id  #first record id
gi|227437129|gb|FJ817486.1|
# print len(records[-1].seq)  #length of the last record
771

"""

