## 백준 16953 A->B

### 풀이과정

- 처음에는 graph를 만들어서 graph[n]에 n로 바꾸는 데 필요한 연산의 최솟값을 더했지만 메모리 초과 에러..
- bfs 탐색 시 큐에 연산의 최솟값을 같이 넣어줌으로서 해결

### 코드 구현

사용 언어 : **파이썬**

```python
from collections import deque

A, B = map(int, input().split())
# a->b로 연산이 되지 않는 경우 -1을 출력하기 위해 초기값 -1로 설정
answer = -1

def bfs(n):
    global answer
    queue = deque()
    # 큐에 연산 횟수를 같이 넣어줌
    queue.append((n, 1))

    while queue:
        node, cnt = queue.popleft()

        # node가 B면 answer를 큐에 같이 들어있었던 연산횟수로 초기화해주고 리턴
        if node == B:
            answer = cnt
            return
        # 2를 곱한 값, 1을 수의 가장 오른쪽에 추가한 값이 B보다 작으면 큐에 연산횟수와 함께 넣어줌
        if node*2 <= B:
            queue.append((node*2, cnt+1))
        if node*10+1 <= B:
            queue.append((node*10+1, cnt+1))
    return

bfs(A)
print(answer)

```
