## 풀이  

BFS를 이용해 풀어주었습니다.  

queue에 시작점(src)를 넣어주며 이미 방문했던 step은 방문하지 않게끔 visited도 같이 넣어주었습니다. dist는 dist가 가질 수 있는 최대 거리인 N+1으로 초기화해주었고 dist를 업데이트해주며 jump가 dist보다 클 경우에는 더이상 찾지 않게 했습니다.  

해당 step이 1의 배수만큼 움직일 수 있다면 더이상 찾지 않게끔 바로 dist를 업데이트 해주었습니다.  

각각 양의 배수와 음의 배수쪽 둘다 확인해주기 위해 for loop을 다른 방향으로 두번 써주어 queue에 넣어주었습니다.  

## 코드  
```python
from collections import deque

N = int(input())
steps = list(map(int, input().split()))
src, dest = map(int, input().split())
visited = [0 for _ in range(N)]
queue = deque([[src, 0, visited]])
dist = N+1

while queue:
    step, jumps, visited = queue.popleft()
    visited[step-1] = 1
    if steps[step-1] == 1:
       dist = min(jumps+1, dist)
    if step != dest and jumps < dist:
        for i in range(step, N+1, steps[step-1]):
            if not visited[i-1]:
                queue.append((i, jumps+1, visited))
        for j in range(step, 0, -steps[step-1]):
            if not visited[j-1]:
                queue.append((j, jumps+1, visited))
    else:
        dist = min(jumps, dist)
     
if dist == N+1: print(-1)
else: print(dist)
```