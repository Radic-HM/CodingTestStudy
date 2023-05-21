from queue import Queue
N = int(input())
graph = []
visit = [[0 for i in range(N)] for j in range(N)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(N):
    a = input()
    graph.append(a)

count_house = 0
houses = []
q = Queue()

# BFS로 풀이
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0 and graph[i][j] == '1':
            count_house += 1
            house_num = 0
            q.put([i, j])
            while not q.empty():
                x, y = q.get()
                # queue에 동일한 좌표가 여러 번 들어가는 경우 생기는 것 방지
                if visit[x][y] == 1:
                    continue
                house_num += 1
                visit[x][y] = 1
                for k in range(4):
                    if 0 <= x+dx[k] < N and 0 <= y+dy[k] < N:
                        if visit[x+dx[k]][y+dy[k]] == 0 and graph[x+dx[k]][y+dy[k]] == '1':
                            q.put([x+dx[k], y+dy[k]])
            houses.append(house_num)

print(count_house)
houses.sort()
for h in houses:
    print(h)
