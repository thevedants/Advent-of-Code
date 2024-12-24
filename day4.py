def check(i,j, grid):
    counter = 0
    L = ['X','M','A','S']
    for k in range(4):
        if(j+k < n and grid[i][j + k] == L[k]):
            pass
        else:
            break
    else:
        counter += 1
    for k in range(4):
        if(j-k >= 0 and grid[i][j - k] == L[k]):
            pass
        else:
            break
    else:
        counter += 1
    for k in range(4):
        if(i+k < m and grid[i+k][j] == L[k]):
            pass
        else:
            break
    else:
        counter += 1
    for k in range(4):
        if(i-k >= 0 and grid[i - k][j] == L[k]):
            pass
        else:
            break
    else:
        counter += 1
    for k in range(4):
        if(j+k < n and i + k < m and grid[i + k][j + k] == L[k]):
            pass
        else:
            break
    else:
        counter += 1
    for k in range(4):
        if(j-k >= 0 and i - k >= 0 and grid[i - k][j - k] == L[k]):
            pass
        else:
            break
    else:
        counter += 1
    for k in range(4):
        if(i+k < m and j - k >= 0 and grid[i+k][j-k] == L[k]):
            pass
        else:
            break
    else:
        counter += 1
    for k in range(4):
        if(j+k < n and i - k >= 0 and grid[i - k][j + k] == L[k]):
            pass
        else:
            break
    else:
        counter += 1
    return counter
def check2(i,j,grid):
    counter = 0
    L = ['M','A','S']
    for k in range(3):
        if(j+k < n and i + k < m and grid[i + k][j + k] == L[k]):
            pass
        else:
            break
    else:
        if grid[i][j + 2] == 'M' and grid[i + 2][j] == 'S' or grid[i][j + 2] == 'S' and grid[i+2][j]== 'M':
            counter += 1
    for k in range(3):
        if(j-k >= 0 and i - k >= 0 and grid[i - k][j - k] == L[k]):
            pass
        else:
            break
    else:
        if grid[i][j - 2] == 'M' and grid[i - 2][j] == 'S' or grid[i][j - 2] == 'S' and grid[i-2][j]== 'M':
            counter += 1
    for k in range(3):
        if(i+k < m and j - k >= 0 and grid[i+k][j-k] == L[k]):
            pass
        else:
            break
    else:
        if grid[i][j - 2] == 'M' and grid[i + 2][j] == 'S' or grid[i][j - 2] == 'S' and grid[i+2][j]== 'M':
            counter += 1
    for k in range(3):
        if(j+k < n and i - k >= 0 and grid[i - k][j + k] == L[k]):
            pass
        else:
            break
    else:
        if grid[i][j + 2] == 'M' and grid[i - 2][j] == 'S' or grid[i][j + 2] == 'S' and grid[i-2][j]== 'M':
            counter += 1
    return counter


with open("day4.txt", "r") as file:
    grid = [list(line.strip()) for line in file]

m = len(grid)
n = len(grid[0])
counter = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == 'X':
            counter += check(i,j,grid)
print("Answer to part 1 =", counter)

counter2 = 0
for i in range(m):
    for j in range(n):
        if grid[i][j] == 'M':
            counter2 += check2(i,j,grid)
print("Answer to part 2 =", counter2//2)


