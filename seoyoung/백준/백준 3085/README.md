## 백준 3085번

### 알고리즘

- **구현**

### 코드 구현

사용 언어 : **파이썬**

```python
N = int(input())
graph = [list(input()) for i in range(N)]
answer = 1

# 최대의 사탕 개수를 리턴하는 함수
def count():
    global answer
    # 가로방향 탐색
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if graph[i][j] == graph[i][j+1]:
                cnt += 1
                # if-else 문 마치고 answer값 초기화해주면 시간 초과남
                answer = max(answer, cnt)
            else:
                # 사탕 색이 같지 않으면 다시 찾아줘야 하므로 cnt를 1로 초기화
                cnt = 1
    #가로 방향 탐색과 같은 방식으로 세로방향 탐색
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if graph[j][i] == graph[j+1][i]:
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt = 1

# 가로방향으로 인접한 칸의 사탕을 교환한 뒤 최대 사탕 개수를 answer에 저장
for i in range(N):
    for j in range(N-1):
        graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
        count()
        graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]

# 세로방향도 같은 방식으로 교환하고 answer값 저장
for i in range(N):
    for j in range(N-1):
        graph[j][i], graph[j+1][i] = graph[j+1][i], graph[j][i]
        count()
        graph[j][i], graph[j+1][i] = graph[j+1][i], graph[j][i]

print(answer)

```
