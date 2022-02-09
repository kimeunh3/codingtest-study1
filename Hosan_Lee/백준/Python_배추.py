import sys

sys.setrecursionlimit(10**6)

def DFS(a, b):
    visited[a][b] += 1
    for i in range(4):
        na = a + x_ach[i]  # nx가 행
        nb = b + y_ach[i]  # ny가 열
        if (0 <= na < depth) and (0 <= nb < width) :
            if visited[na][nb] == 0 and field[na][nb] == 1:
                DFS(na, nb)

T = int(input())
for i in range(T):
    str = input().split()
    width = int(str[0])  # 가로 M
    depth = int(str[1])  # 세로 N
    Number = int(str[2])  # 배추의 포기수 K

    field = [[0 for i in range(width)] for j in range(depth)]
    visited = [[0 for i in range(width)] for j in range(depth)]

    for j in range(Number):
        m, n = map(int, input().split())
        field[n][m] = 1

    y_ach = [1, -1, 0, 0]
    x_ach = [0, 0, 1, -1]
    count = 0

    for a in range(depth):  # a가 열
        for b in range(width):  # B가 행
            if visited[a][b] == 0 and field[a][b] == 1:
                count += 1
                DFS(a, b)
    print(count)
