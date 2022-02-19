N = int(input())
board = [list(input()) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def check(board, i, y, x):
    result = 0
    if dy[i]: # y-1, y+1
        # 행 체크
        for i in [-1, 1]:
            if 0 <= y + i < N:
                prev = board[y + i][0]
                prev_i = 0
                for j in range(N):
                    if prev != board[y + i][j]:
                        prev = board[y + i][j]
                        result = max(result, j - prev_i)
                        prev_i = j
                result = max(result, N - prev_i)
        
        # 열 체크
        prev = board[x][0]
        prev_i = 0
        for j in range(N):
            if prev != board[j][x]:
                prev = board[j][x]
                result = max(result, j - prev_i)
                prev_i = j
        result = max(result, N - prev_i)
    else:
        # 행 체크
        prev = board[y][0]
        prev_i = 0
        for j in range(N):
            if prev != board[y][j]:
                prev = board[y][j]
                result = max(result, j - prev_i)
                prev_i = j
        result = max(result, N - prev_i)
        # 열 체크
        for i in [-1, 1]:
            if 0 <= x + i < N:
                prev = board[0][x+i]
                prev_i = 0
                for j in range(N):
                    if prev != board[j][x+i]:
                        prev = board[j][x+i]
                        result = max(result, j - prev_i)
                        prev_i = j
                result = max(result, N - prev_i)

    return result

result = 0

for y in range(N):
    if result == N:
            break
    for x in range(N):
        if result == N:
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and board[y][x] != board[ny][nx]:
                # swap
                board[y][x], board[ny][nx] = board[ny][nx], board[y][x]
                result = max(result, check(board, i, y, x))
                # swap back
                board[y][x], board[ny][nx] = board[ny][nx], board[y][x]

print(result)