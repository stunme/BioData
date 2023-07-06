with open("test.txt",'r') as f:
    page = f.read()

import re
for i in re.split('{"|,"',page):
    cur = i.replace('"','').split(':')
    if cur[0] =="name":
        
        print(cur[1])


