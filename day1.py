import math
numbers1 = []
numbers2 = []
with open('day1.txt', 'r') as file:
    for line in file:
        num1, num2 = map(float, line.split())
        numbers1.append(num1)
        numbers2.append(num2)

numbers1.sort()
numbers2.sort()
counter = 0
n = len(numbers1)
for i in range(n):
    counter += math.fabs(numbers1[i] - numbers2[i])
print("Answer to part 1 =", int(counter))

M = {}
for i in range(n):
    if i != 0 and numbers2[i - 1] == numbers2[i]:
        M[numbers2[i]] += 1
    else:
        M[numbers2[i]] = 1
counter2 = 0
for i in range(n):
    counter2 += numbers1[i] * M.get(numbers1[i], 0)
print("Answer to part 2 =", int(counter2))