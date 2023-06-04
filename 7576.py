from collections import deque
# queue보다 deque가 빠르다고 함

M, N = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# queue에 count값을 넣어서 사용하는 경우 시간초과 발생함
# graph 좌표에 count값을 저장해서 최댓값 구하면 시간초과 발생 X
q = deque()

for i in range(N):
    a = list(map(int, input().split()))
    graph.append(a)
    for idx, j in enumerate(a):
        if j == 1:
            q.append([i, idx])

ans = 0

for row in graph:
    if 0 in row:
        ans = -1

# 토마토가 모두 익은 경우 / 모든 칸이 비어있는 경우
if ans == 0:
    print(ans)
    exit()

while q:
    x, y = q.popleft()
    for i in range(4):
        new_x = x+dx[i]
        new_y = y+dy[i]
        if 0 <= new_x < N and 0 <= new_y < M and graph[new_x][new_y] == 0:
                q.append([new_x, new_y])
                graph[new_x][new_y] = graph[x][y] + 1

for row in graph:
    if 0 in row:
        print(-1)
        exit()
    else:
        ans = max(ans, max(row)-1)
print(ans)

