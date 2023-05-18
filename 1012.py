import sys
sys.setrecursionlimit(10**6)

T = int(input())

graph = [[0 for i in range(50)] for i in range(50)]
visit = [[0 for i in range(50)] for i in range(50)]
count = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def search(x, y, M, N):
    if visit[x][y] == 0 and graph[x][y] == 1:
        visit[x][y] = 1
        for i in range(4):
            if 0 <= x + dx[i] < M and 0 <= y + dy[i] < N:
                search(x + dx[i], y + dy[i], M, N)


while T > 0:
    T -= 1
    M, N, K = map(int, input().split())
    graph = [[0 for i in range(N)] for i in range(M)]
    visit = [[0 for i in range(N)] for i in range(M)]
    count = 0
    baechu_li = []
    for i in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1
        baechu_li.append([a, b])

    for baechu in baechu_li:
        if visit[baechu[0]][baechu[1]] == 0:
            search(baechu[0], baechu[1], M, N)
            count += 1

    print(count)
