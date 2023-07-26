##  Strings and Lists

"""
Problem
Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d
 (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

Sample Dataset
HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102

Sample Output
Humpty Dumpty
"""

with open("../Datasets/INI3_dataset.txt",'r') as f:
    s = f.readline().strip()
    a,b,c,d = map(int,f.readline().strip().split())

print(" ".join([s[a:b+1],s[c:d+1]]))
