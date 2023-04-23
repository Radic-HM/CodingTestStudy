import copy

N = int(input())
li = []
row = 0
col = 0

for i in range(N):
    l = list(input())
    li.append(l)

map = copy.deepcopy(li)
for i in range(N):
    for j in range(N-1):
        if map[i][j] == '.' and map[i][j+1] == '.':
            row += 1
            k = j
            while k < N and map[i][k] == '.':
                map[i][k] = 'X'
                k += 1

map = li.copy()
for i in range(N):
    for j in range(N-1):
        if map[j][i] == '.' and map[j+1][i] == '.':
            col += 1
            k = j
            while k < N and map[k][i] == '.':
                map[k][i] = 'X'
                k += 1

print(row, col)
