import sys
sys.setrecursionlimit(10**6)
# DFS 사용 시 recursion limit 주의
# pypy에서 import sys하면 메모리 초과 주의

N, M, K = map(int, input().split())

graph = [[0 for i in range(N)] for i in range(M)]
visit = [[0 for i in range(N)] for i in range(M)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

answer = []

# count 변수 전역으로 사용하려다가 안돼서 방법 바꿈
def search(x, y, count):
    visit[x][y] = 1
    for i in range(4):
        if 0 <= x+dx[i] < M and 0 <= y+dy[i] < N:
            if visit[x+dx[i]][y+dy[i]] == 0 and graph[x+dx[i]][y+dy[i]] == 0:
                count += 1
                count = search(x+dx[i], y+dy[i], count)
    return count


for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[x][y] = 1
for x in range(M):
    for y in range(N):
        if graph[x][y] == 0 and visit[x][y] == 0:
            count = 1
            count = search(x, y, count)
            answer.append(count)
answer.sort()
print(len(answer))
for a in answer:
    print(a, end=' ')


