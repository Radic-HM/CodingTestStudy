N = int(input())
channels = []
cur_idx = 0

KBS1_idx = 0
KBS2_idx = 0

for i in range(N):
    channel_name = input()
    if channel_name == 'KBS1':
        KBS1_idx = i
    elif channel_name == 'KBS2':
        KBS2_idx = i
# 채널 내리기(1), 위 채널과 바꾸기(4)만 사용
print('1'*KBS1_idx, end='')
print('4'*KBS1_idx, end='')

# 만약 KBS1의 index가 KBS2의 index보다 큰 경우 KBS2의 index가 하나 더 커지게됨
if KBS1_idx > KBS2_idx:
    KBS2_idx += 1

print('1'*KBS2_idx, end='')
print('4'*(KBS2_idx-1), end='')

