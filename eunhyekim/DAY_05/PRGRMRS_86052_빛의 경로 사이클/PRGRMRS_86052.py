# 상: 0, 하: 1, 좌: 2, 우: 3
def turnRight(grid, d, y, x):
    nd, ny, nx = 0, 0, 0
    lenY, lenX = len(grid), len(grid[0])
    if d == 0:
        ny = y
        nx = (lenX + x - 1) % lenX
        nd = 3
    elif d == 1:
        ny = y
        nx = (x + 1) % lenX
        nd = 2
    elif d == 2:
        ny = (y + 1) % lenY
        nx = x
        nd = 0
    else:
        ny = (lenY + y - 1) % lenY
        nx = x
        nd = 1

    return nd, ny, nx
    
def turnLeft(grid, d, y, x):
    nd, ny, nx = 0, 0, 0
    lenY, lenX = len(grid), len(grid[0])
    if d == 0:
        ny = y
        nx = (x + 1) % lenX
        nd = 2
    elif d == 1:
        ny = y
        nx = (lenX + x - 1) % lenX
        nd = 3
    elif d == 2:
        ny = (lenY + y - 1) % lenY
        nx = x
        nd = 1
    else:
        ny = (y + 1) % lenY
        nx = x
        nd = 0

    return nd, ny, nx

def goStraight(grid, d, y, x):
    nd, ny, nx = 0, 0, 0
    lenY, lenX = len(grid), len(grid[0])
    if d == 0:
        ny = (y + 1) % lenY
        nx = x
        nd = 0
    elif d == 1:
        ny = (lenY + y - 1) % lenY
        nx = x
        nd = 1
    elif d == 2:
        ny = y
        nx = (x + 1) % lenX
        nd = 2
    else:
        ny = y
        nx = (lenX + x - 1) % lenX
        nd = 3

    return nd, ny, nx

def move(ch, grid, d, y, x):
    if ch == "S":
        return goStraight(grid, d, y, x)
    elif ch == "R":
        return turnRight(grid, d, y, x)
    else:
        return turnLeft(grid, d, y, x)
        

def solution(grid):
    answer = []
    visited = [ [ [0, 0, 0, 0] for _ in range(len(grid[0])) ] for _ in range(len(grid)) ]
    total_path = len(grid)*len(grid[0])*4
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                if visited[i][j][k]:
                    continue
                cnt = 0
                d, y, x = k, i, j
                while True:
                    if visited[y][x][d]:
                        if y == i and x == j:
                            answer.append(cnt)
                        break
                    cnt += 1
                    visited[y][x][d] = 1
                    d, y, x = move(grid[y][x], grid, d, y, x)
    answer.sort()
    return answer