T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    distance = y-x
    repeat = 1

    while True:
        if distance <= repeat*(repeat+1):
            break
        repeat += 1

    if distance > repeat**2:
        print(repeat*2)
    else:
        print(repeat*2-1)
