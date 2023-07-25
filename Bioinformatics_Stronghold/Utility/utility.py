def readFastaFileDict(path):
    res = {}
    label = ""
    tmp = ""
    with open(path, 'r') as f:
        for l in f.readlines():
            tmpLine = l.strip()
            if tmpLine[0] == '>':
                if not tmp == "":
                    res[label] = tmp
                label = tmpLine[1:]
                tmp = ""
            else:
                tmp += tmpLine
        if not tmp == "":
            res[label] = tmp
    return res

def readFastaFileList(path):
    res = []
    label = ""
    tmp = ""
    with open(path, 'r') as f:
        for l in f.readlines():
            tmpLine = l.strip()
            if tmpLine == "":
                continue
            if tmpLine[0] == '>':
                if not tmp == "":
                    res.append(tmp)
                label = tmpLine[1:]
                tmp = ""
            else:
                tmp += tmpLine
        if not tmp == "":
            res.append(tmp)
    return res

