## 풀이  

BFS를 이용하여 풀었습니다.  

방문할 때마다 cnt를 늘려주었고, 상하좌우에 1이 있는지 확인해주며 queue에 추가해주었습니다. queue에 추가하는 순간 field의 값을 0으로 바꿔주면서 중복하여 추가하지 않게끔 했습니다.  
함수 마지막에는 세어준 cnt를 return해주었고 해당 cnt를 단지마다 찾아 cnt_lst에 넣어주었습니다.  

cnt_lst의 길이와 정렬된 cnt_lst를 한 줄에 하나씩 출력해주었습니다.  

## 코드  
```python
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
field = [ list(map(int, list(input().strip()))) for _ in range(N) ]

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

cnt_lst = []

def bfs(x, y):
    queue = deque([(x, y)])
    field[y][x] = 0 
    cnt = 0
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and field[ny][nx]:
                queue.append((nx, ny))
                field[ny][nx] = 0 
    return cnt

for y in range(N):
    for x in range(N):
        if field[y][x]:
            cnt_lst.append(bfs(x, y))

print(len(cnt_lst))
print(*sorted(cnt_lst), sep="\n")
```