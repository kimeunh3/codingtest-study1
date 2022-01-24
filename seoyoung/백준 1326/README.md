## 백준 1326번 폴짝폴짝

### 문제 설명

- 징검다리에 쓰여 있는 수의 배수만큼 떨어져 있는 곳으로 갈 수 있는 개구리
- 이 개구리가 a번째 징검다리에서 b번째 징검다리로 가려고 할 때의 최소 점프 횟수 구하기

### 알고리즘

- **bfs**

### 풀이 과정

```txt
✅ 시작 징검다리를 기준으로 조건(징검다리에 쓰여있는 배수만큼 떨어져 있는 곳으로 갈 수 있음)을 만족하는 징검다리로 갈 수 있는 점프 횟수를 visited 배열에 저장함
✅ 조건을 만족함과 동시에 그 징검다리의 번호가 b이면 for문과 while문을 빠져나가서 visited[b]를 출력하도록 한다.

❓ 다이나믹 프로그래밍으로도 풀 수 있지 않을까,,?
```

### 코드 구현

사용 언어 : **파이썬**

```python
from collections import deque

N = int(input())
bridge = list(map(int, input().split()))
a, b = map(int, input().split())

# 방문 여부를 포함하여 점프 횟수를 저장할 배열
visited = [-1]*(N+1)
# break문에 빠져나왔는지의 여부를 확인하기 위한 변수
flag = False

# 큐에 시작점 a를 넣고 방문 처리
queue = deque()
queue.append(a)
visited[a] = 0

while queue:
    # 현재 징검다리 번호
    node = queue.popleft()

    for i in range(1, N+1):
        # 징검다리 번호 i가 현재 징검다리(node)에 쓰여있는 배수만큼 떨어져 있는가?
        # 아직 건너지 않은 징검다리인가?(만약 건넜으면 이미 최소점프횟수가 저장되어 있기 때문에 살펴보지 않아도 됨)
        if (i-node) % bridge[node-1] == 0 and visited[i] == -1:
            queue.append(i)
            visited[i] = visited[node]+1
            # 만약 위의 조건을 만족함과 동시에 살펴보고 있는 징검다리가 b이면 이제 while문을 종료하면 됨
            if i == b:
                flag = True
                break
    if flag:
        break

print(visited[b])
```
