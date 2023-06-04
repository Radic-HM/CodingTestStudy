from collections import deque

N, M = map(int, input().split())

graph = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque([])

for i in range(N):
    a = list(map(int, input()))
    graph.append(a)
q.append([0, 0])

while q:
    x, y = q.popleft()
    for i in range(4):
        new_x = x+dx[i]
        new_y = y+dy[i]
        if 0 <= new_x < N and 0 <= new_y < M and graph[new_x][new_y] == 1:
            graph[new_x][new_y] = graph[x][y] + 1
            q.append([new_x, new_y])

print(graph[N-1][M-1])
