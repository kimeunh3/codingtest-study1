def add_digit(digit, num):
    if digit == 1:
        decreasing.append(num)
    else:
        for i in range(num % 10):
            add_digit(digit - 1, num * 10 + i)

def backtracking(digit):
    for i in range(digit - 1, 10):
        add_digit(digit, i)

decreasing = []
for i in range(1, 11):
    backtracking(i)
n = int(input())
if n >= len(decreasing):
    print(-1)
else:
    print(decreasing[n])