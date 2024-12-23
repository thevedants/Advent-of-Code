import math

def check(i):
    if sorted(i, reverse=True) == i or sorted(i) == i:
        for j in range(1,len(i)):
            if math.fabs(i[j] - i[j - 1]) > 0 and math.fabs(i[j] - i[j - 1]) < 4:
                pass
            else:
                return False
        else:
            return True
    else:
        return False
reports = []

with open('day2.txt', 'r') as file:
    for line in file:
        num= list(map(float, line.split()))
        reports.append(num)
counter = 0
for i in reports:
    if check(i):
        counter += 1
    
print("Answer to part 1 =", counter)

counter2 = 0

for i in reports:
    if check(i):
        counter2 += 1
    else:
        for j in range(len(i)):
            temp = i[:j] + i[j+1:]
            if check(temp):
                counter2 += 1
                break
print("Answer to part 2 =", counter2)





