def check_prime(num):
    for i in range(2, N):
        if num % i < 1:
            return False
    return True

def check_palindrome(num):
    num_to_str = str(num)
    for i in range(len(num_to_str)//2+1):
        if num_to_str[i] != num_to_str[-(i+1)]:
            return False
    return True

N = int(input())

while True:
    # 1은 소수가 아님
    if N == 1:
        print(2)
        break
    # and 로 2개의 조건을 사용할 때 앞에 있는 조건을 먼저 검사
    # 팰린드롬 여부 판단이 더 빠른 연산으로 먼저 검사하면 시간 초과 X
    if check_palindrome(N) and check_prime(N):
        print(N)
        break
    else:
        N += 1
