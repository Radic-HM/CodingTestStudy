N = int(input())
computers = [[0 for i in range(N+1)] for i in range(N+1)]
virus = [0 for i in range(N+1)]


def dfs(idx):
    for i in range(1, N+1):
        if idx != i and virus[i] == 0 and computers[idx][i] == 1:
            virus[i] = 1
            dfs(i)


M = int(input())
for i in range(M):
    u, v = map(int, input().split())
    computers[u][v] = 1
    computers[v][u] = 1

virus[1] = 1
dfs(1)
print(sum(virus)-1)
