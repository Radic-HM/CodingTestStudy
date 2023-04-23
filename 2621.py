cards = []
colors = []
colors_count = [0 for i in range(4)]
numbers = []
numbers_count = [0 for i in range(10)]
score = 0
for i in range(5):
    a = input()
    color, num = a.split(' ')
    colors.append(color)
    numbers.append(int(num))
    cards.append([color, num])
    numbers_count[int(num)] += 1
    if color == 'R': colors_count[0] += 1
    elif color == 'B': colors_count[1] += 1
    elif color == 'Y': colors_count[2] += 1
    elif color == 'G': colors_count[3] += 1


def straight(numbers):
    numbers.sort()
    for i in range(4):
        if numbers[i+1] - numbers[i] != 1:
            return False
    return True


if len(set(colors)) == 1 and straight(numbers):
    score += 900
    score += max(numbers)
elif max(numbers_count) == 4:
    score += 800
    for i in range(1, 10):
        if numbers_count[i] == 4:
            score += i
            break
elif 3 in numbers_count and 2 in numbers_count:
    score += 700
    for i in range(1, 10):
        if numbers_count[i] == 2:
            score += i
        if numbers_count[i] == 3:
            score += i*10
elif len(set(colors)) == 1:
    score += 600
    score += max(numbers)
elif straight(numbers):
    score += 500
    score += max(numbers)
elif 3 in numbers_count:
    score += 400
    for i in range(1, 10):
        if numbers_count[i] == 3:
            score += i
elif numbers_count.count(2) == 2:
    score += 300
    same_numbers = []
    for i in range(1, 10):
        if numbers_count[i] == 2:
            same_numbers.append(i)
    score += min(same_numbers)
    score += max(same_numbers) * 10
elif 2 in numbers_count:
    score += 200
    for i in range(1, 10):
        if numbers_count[i] == 2:
            score += i
else:
    score += 100
    score += max(numbers)


print(score)
