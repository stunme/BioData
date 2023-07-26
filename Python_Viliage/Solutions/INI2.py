##  Variables and Some Arithmetic

"""
Problem
Given: Two positive integers a
 and b
, each less than 1000.

Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a
 and b
.

Notes:

The dataset changes every time you click "Download dataset".
We check only your final answer to the downloaded dataset in the box below, not your code itself. If you would like to provide your code as well, you may use the upload tool. Please also note that the correct answer to this problem will not in general be 34; it is simply an example of what you should return in the specific case that the legs of the triangle have length 3 and 5.
Sample Dataset
3 5
Sample Output
34
"""

with open("../Datasets/INI2_dataset.txt",'r') as f:
    a,b = map(int,f.readline().strip().split())

print(a**2+b**2)
