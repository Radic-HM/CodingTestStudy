import sys
sys.setrecursionlimit(10**6)

N = int(input())

graph = []
graph_2 = []
visit = [[0 for i in range(N)] for j in range(N)]
visit_2 = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    a = input()
    graph.append(a)
    b = a.replace('G', 'R')
    graph_2.append(b)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

count_r_g_b = 0
count_rg_b = 0

def dfs(x, y, v, color_, graph_):
        for i in range(4):
            if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N:
                if v[x+dx[i]][y+dy[i]] == 0 and graph_[x+dx[i]][y+dy[i]] == color_:
                    v[x+dx[i]][y+dy[i]] = 1
                    dfs(x+dx[i], y+dy[i], v, color_, graph_)

for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            count_r_g_b += 1
            color = graph[i][j]
            visit[i][j] = 1
            dfs(i, j, visit, color, graph)

for i in range(N):
    for j in range(N):
        if visit_2[i][j] == 0:
            count_rg_b += 1
            color = graph_2[i][j]
            visit_2[i][j] = 1
            dfs(i, j, visit_2, color, graph_2)

print(count_r_g_b, count_rg_b)
