N = int(input())

ans = 1
new_number = N % 10 + N // 10
new_number = N % 10 * 10 + new_number % 10
while new_number != N:
    ans += 1
    a = new_number % 10 + new_number // 10
    new_number = new_number % 10 * 10 + a % 10
    # print(new_number)
print(ans)
