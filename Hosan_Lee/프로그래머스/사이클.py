def solution(grid):

    direction = [[-1, 0], [1, 0], [0, 1], [0, -1]] # 왼 오른 아래 위, 첫번째 인덱스는 y좌표, 두번째 인덱스는 x좌표

    right = {0: 3, 1: 2, 2: 0, 3: 1}
    left = {0: 2, 1: 3, 2: 1, 3: 0}
    answer = []
    width, height = len(grid[0]), len(grid) # 가로 길이 'RL' 이라면 2, 세로 길이 원소의 개수

    possibility = [[[1] * 4 for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            for i in range(4):
                if possibility[y][x][i] == 0:
                    continue
                cnt = 0  # 사이클의 길이
                curr_y, curr_x, curr_i = y, x, i
                while True:
                    possibility[curr_y][curr_x][curr_i] -= 1
                    cnt += 1
                    curr_alphabet = grid[curr_y][curr_x] # 알파벳을 확인한다.

                    if curr_alphabet == 'R':
                        curr_i = right[curr_i]
                    elif curr_alphabet == 'L':
                        curr_i = left[curr_i]
                    curr_x, curr_y = (curr_x + direction[curr_i][1]) % width, (curr_y + direction[curr_i][0]) % height #width, height 로 나눠주는 이유 : 끝에 갔다면 처음으로
                    # 처음 출발점에 왔다면 break 후 다음 탐색
                    if curr_x == x and curr_y == y and curr_i == i:
                        break
                answer.append(cnt)
    answer.sort()
    return answer