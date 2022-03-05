## 백준 1697번 숨바꼭질

## 문제 풀이

```
✅ N->K이지만 K보다 큰 지점에서 K로 올 수도 있음
 ➡️ 현재 위치를 중심으로 갈 수 있는 위치를 계산할 때 0<=현재위치<=K 가 아니라 0 <=i<=100000임을 염두에 둬야 하는 문제
 ➡️ 그래서 distance 배열도 크기를 100001로 해줘야 함
```

### 코드 구현

사용 언어 : **파이썬**

```python
from collections import deque

N, K = map(int, input().split())

distance = [0]*100001

def bfs(v):
    queue = deque()
    queue.append(v)

    while queue:
        node = queue.popleft()

        if node == K:
            print(distance[node])
            break

        for i in (node-1, node+1, node*2):
            if 0 <= i <= 100000 and distance[i] == 0:
                distance[i] = distance[node]+1
                queue.append(i)


bfs(N)

```
