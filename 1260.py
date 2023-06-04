from queue import Queue
import sys
sys.setrecursionlimit(10**6)

N, M, V = map(int, input().split())

graph = [[0 for i in range(N+1)] for j in range(N+1)]

dfs_visit_order = [V]
bfs_visit_order = []

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


dfs_visit = [0 for i in range(N+1)]
dfs_visit[V] = 1

bfs_visit = [0 for i in range(N+1)]

def dfs(x, y):
    dfs_visit_order.append(y)
    dfs_visit[y] = 1
    for i in range(1, N+1):
        if graph[y][i] == 1 and dfs_visit[i] == 0:
            dfs(y, i)

for i in range(1, N+1):
    if graph[V][i] == 1 and dfs_visit[i] == 0:
        dfs(V, i)

q = Queue()
q.put(V)

while not q.empty():
    x = q.get()
    if bfs_visit[x] == 1:
        continue
    bfs_visit[x] = 1
    bfs_visit_order.append(x)
    for i in range(1, N+1):
        if graph[x][i] == 1 and bfs_visit[i] == 0:
            q.put(i)

for v in dfs_visit_order:
    print(v, end=' ')
print()
for v in bfs_visit_order:
    print(v, end=' ')
