from queue import Queue

N, K = map(int, input().split())
visit = [0 for i in range(100001)]
q = Queue()

q.put([N, 0])

while not q.empty():
    x, count = q.get()
    if x == K:
        print(count)
        break
    if visit[x] == 1:
        continue
    visit[x] = 1
    movement = [x-1, x+1, x*2]
    for y in movement:
        if 0 <= y < 100001:
            q.put([y, count+1])

# BFS 이용해서 푸는 문제
