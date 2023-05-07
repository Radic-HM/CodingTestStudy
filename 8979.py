N, K = map(int, input().split())

scores = []
target_score = []

for i in range(N):
    score = list(map(int, input().split()))
    scores.append(score)
    if score[0] == K:
        target_score = score

# 점수 각각을 정렬하는 방법 사용

# scores = sorted(scores, key=lambda x: x[3], reverse=True)
# scores = sorted(scores, key=lambda x: x[2], reverse=True)
# scores = sorted(scores, key=lambda x: x[1], reverse=True)
scores.sort(key=lambda x: (-x[1], -x[2], -x[3]))  # -> 이렇게 사용해도 됨

for i in range(N):
    if scores[i][1] == target_score[1] and scores[i][2] == target_score[2] and scores[i][3] == target_score[3]:
        print(i + 1)
        break
