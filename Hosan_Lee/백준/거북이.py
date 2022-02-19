import sys

input = sys.stdin.readline
T = int(input().rstrip())
pos = [(0, 1), (-1, 0), (0, -1), (1, 0)]

for t in range(T):
    cur = [0, 0]
    rotate = 0
    min_xy = [0, 0]
    max_xy = [0, 0]
    cmd = input().rstrip()
    for c in cmd:
        if c == "F":  # 전진
            cur[0] += pos[rotate][0]
            cur[1] += pos[rotate][1]
        elif c == "B":  # 후진
            cur[0] -= pos[rotate][0]
            cur[1] -= pos[rotate][1]
        elif c == "L":
            if rotate == 3:
                rotate = 0
            else:
                rotate += 1
        elif c == "R":
            if rotate == 0:
                rotate = 3
            else:
                rotate -= 1
        if min_xy[0] > cur[0]:
            min_xy[0] = cur[0]
        elif max_xy[0] < cur[0]:
            max_xy[0] = cur[0]
        if min_xy[1] > cur[1]:
            min_xy[1] = cur[1]
        elif max_xy[1] < cur[1]:
            max_xy[1] = cur[1]

    print((max_xy[0] - min_xy[0]) * (max_xy[1] - min_xy[1]))