## 백준 2606번 바이러스

### 알고리즘

- **BFS**

### 코드 구현

사용 언어 : **파이썬**

```python
from collections import deque

N = int(input())
M = int(input())
graph = [[] for i in range(N+1)]

# n - m 컴퓨터가 연결된 경우
# n번째 배열에 m추가, m번째 배열에 n 추가하여 연결성 표현
for i in range(M):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)
answer = 0
visited = []

queue = deque()
# 1번 컴퓨터가 바이러스가 걸린 경우만 체크해주면 되므로 큐에 1을 넣어주고
# BFS로 방문하지 않은 인접한 컴퓨터들을 발견할 때마다 answer+=1 해주면 됨
queue.append(1)
visited.append(1)

while queue:
    node = queue.popleft()
    for n in graph[node]:
        if n not in visited:
            queue.append(n)
            visited.append(n)
            answer += 1

print(answer)


```
