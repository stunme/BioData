##  Finding a Protein Motif
##  python 2.7


"""
Problem
To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means "either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as N{P}[ST]{P}.

You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database, by inserting the ID number into

http://www.uniprot.org/uniprot/uniprot_id
Alternatively, you can obtain a protein sequence in FASTA format by following

http://www.uniprot.org/uniprot/uniprot_id.fasta
For example, the data for protein B5ZC00 can be found at http://www.uniprot.org/uniprot/B5ZC00.

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of locations in the protein string where the motif can be found.

Sample Dataset
A2Z669
B5ZC00
P07204_TRBM_HUMAN
P20840_SAG1_YEAST

Sample Output
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
"""

## define function
import urllib2, time

def readUniportFasta(id):
    url_start = 'http://www.uniprot.org/uniprot/'
    url = url_start + id + '.fasta'

    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-us,en;q=0.5",
        "Accept-Charset": "utf-8",
        "Accept-Encoding": "gzip, deflate",
    }
    user_agent = "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.5) Gecko/20091123 Iceweasel/3.5.5 (like Firefox/3.5.5; Debian-3.5.5-1)"
    request = urllib2.Request(url)
    request.add_header('User-agent', user_agent)
    try:
        response=urllib2.urlopen(request)
    except:
        print "failed to open the url of ID=" + id
        response = None
    return response

def readIDlistDic(idList):
    seq = {}
    for i in idList:
        response = readUniportFasta(i.split("_")[0])
        if response == None:
            seq[i]=""
            continue
        title = response.readline()
        seq[i] = ''.join(l.strip() for l in response.readlines())
        time.sleep(5)
    return seq

def findNGlyco(seq):
    idx = []
    length = 4
    for i in range(len(seq)+1-length):
        if seq[i] == 'N' and seq[i+2] in 'ST' and seq[i+1]!='P' and seq[i+3]!='P':
            idx.append(i+1)
    return idx

##  input dataset
with open("../datasets/MPRT_dataset.txt",'r') as f:
    idList = [i.strip() for i in f.readlines()]

##  print output
result = {}
for key,seq in readIDlistDic(idList).items():
    tmp = findNGlyco(seq)
    if len(tmp)>0:
        print(key)
        print(" ".join(map(str,tmp)))
