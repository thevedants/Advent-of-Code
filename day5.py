with open("day5.txt", "r") as file:
    lines = file.readlines()

separator_index = lines.index("\n")  
section1 = lines[:separator_index]
section2 = lines[separator_index + 1:]
correct = []

pairs = [line.strip().split('|') for line in section1]
parsed_pairs = [(int(x), int(y)) for x, y in pairs]  

parsed_numbers = [list(map(int, line.strip().split(','))) for line in section2]

dep = {}
for i in pairs:
    if int(i[0]) not in dep:
        dep[int(i[0])] = [int(i[1]),]
    else:
        dep[int(i[0])].append(int(i[1]))


for i in parsed_numbers:
    flag = False
    for j in range(len(i)):
        if i[j] in dep:
            for k in dep[i[j]]:
                if k in i[:j]:
                    flag = True
                    break
    if flag:
        pass
    else:
        correct.append(i)
sumer = 0
for i in correct:
    sumer += i[len(i)//2]
print("Answer to part 1 =", sumer)
sumer2 = 0
for i in parsed_numbers:
    if i not in correct:
        S = {}
        for j in i:
            if j in dep:
                for k in dep[j]:
                    if k in i:
                        if j in S:
                            S[j] += 1
                        else:
                            S[j] = 1
        sorted_keys = [key for key, value in sorted(S.items(), key=lambda item: item[1], reverse=True)]
        for j in i:
            if j not in sorted_keys:
                sorted_keys.append(j)
        sumer2 += sorted_keys[len(sorted_keys)//2]
print("Answer to part 2 =", sumer2)
