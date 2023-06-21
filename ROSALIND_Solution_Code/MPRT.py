##  Finding a Protein Motif
##  python 2.7


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

with open("test.txt",'r') as f:
    idList = [i.strip() for i in f.readlines()]

result = {}
for key,seq in readIDlistDic(idList).items():
    tmp = findNGlyco(seq)
    if len(tmp)>0:
        print(key)
        print(" ".join(map(str,tmp)))
