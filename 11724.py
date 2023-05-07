N, M = map(int, input().split())

graph = [[0 for i in range(N + 1)] for i in range(N + 1)]
visit = [0 for i in range(N + 1)]

connected_components = 0


def dfs(idx):
    for i in range(1, N + 1):
        if visit[i] == 0 and graph[idx][i] == 1 and idx != i:
            visit[i] = 1
            # print(idx, i)
            dfs(i)


for i in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1
    # print(graph)

ans = 0

for i in range(1, N + 1):
    # print(visit)
    if visit[i] == 0 and 1 in graph[i]:
        visit[i] = 1
        dfs(i)
        ans += 1

# 다른 정점 연결되지 않은 정점은 연결 요소에 포함시켜야함
print(ans + visit.count(0) - 1)

# python3보다 pypy가 속도가 빨라서 pypy로 제출하면 시간 초과 안생김
