'''백준 단지번호 2667번

- 각 단지를 구별하기 위해 1이 이어지는 곳을 한번에 탐색하고자 dfs 사용
- 지나가는 자리는 0으로 바꿔주며 visited 처리
- 1하나를 지날 때마다 cnt를 +1 해주며 각 단지별 cnt를 구함
- cnt 변수를 global로 설정해 함수 밖에서도 값에 접근할 수 있게 함
'''

def get_danji(n, x, y, danji):
    global cnt
    cnt += 1
    danji[x][y] = 0
    mx = [-1, 1, 0, 0]
    my = [0, 0, -1, 1]

    for i in range(4):
        nx = x + mx[i]
        ny = y + my[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if danji[nx][ny] == 1:
            get_danji(n, nx, ny, danji)
    

n = int(input())
danji = []
for _ in range(n):
    danji.append(list(map(int, input())))

result = []
for x in range(n):
    for y in range(n):
        if int(danji[x][y]) == 1:
            cnt = 0
            get_danji(n, x, y, danji)
            result.append(cnt)

print(len(result))
for d in sorted(result):
    print(d)