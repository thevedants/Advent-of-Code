import math
import re
s = ""
pattern = r'mul\(\d{1,3},\d{1,3}\)'
with open('day3.txt', 'r') as file:
    for line in file:
        s += line
matches = (re.findall(pattern, s))

sumer = 0
for i in matches:
    sr = i[4:-1]
    a = sr.split(',')
    x = int(a[0])
    y = int(a[1])
    sumer += (x*y)
print("Answer to part 1 =", sumer)

sumer2 = 0
pattern2 = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
matches2 = re.findall(pattern2, s)
flag = True
for i in matches2:
    if i == "do()":
        flag = True
    elif i == "don't()":
        flag = False
    else:
        if flag:
            sr = i[4:-1]
            a = sr.split(',')
            x = int(a[0])
            y = int(a[1])
            sumer2 += (x*y)
print("Answer to part 2 =",sumer2)



