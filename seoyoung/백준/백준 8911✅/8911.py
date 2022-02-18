N = int(input())
control = [input() for i in range(N)]

for con in control:
    x, y = 0, 0
    point = [{0}, {0}]
    dir = 3
    for c in con:
        if c == 'F':
            if dir == 0:
                x += 1
            elif dir == 1:
                x -= 1
            elif dir == 2:
                y -= 1
            else:
                y += 1
        elif c == 'B':
            if dir == 0:
                x -= 1
            elif dir == 1:
                x += 1
            elif dir == 2:
                y += 1
            else:
                y -= 1
        elif c == 'L':
            if dir == 0:
                dir = 3
            elif dir == 1:
                dir = 2
            elif dir == 2:
                dir = 0
            else:
                dir = 1
        else:  # c=='R'
            if dir == 0:
                dir = 2
            elif dir == 1:
                dir = 3
            elif dir == 2:
                dir = 1
            else:
                dir = 0

        point[0].add(x)
        point[1].add(y)

    max_x, min_x = max(point[0]), min(point[0])
    max_y, min_y = max(point[1]), min(point[1])

    print((max_x-min_x)*(max_y-min_y))
