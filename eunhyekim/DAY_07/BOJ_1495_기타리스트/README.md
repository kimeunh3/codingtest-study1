## 풀이  



## 코드  
```python
N, S, M = map(int, input().split())
V = list(map(int, input().split()))
cache = [[0 for _ in range(M+1)] for _ in range(N+1) ]

# 시작 볼륨 설정
cache[0][S] = 1

for i in range(1, N+1):
    for j in range(M+1):
        if cache[i-1][j] == 0:
            continue
        if j - V[i-1] >= 0:
            cache[i][j - V[i-1]] = 1
        if j + V[i-1] <= M:
            cache[i][j + V[i-1]] = 1
for k in range(M, -1, -1):
    if cache[N][k]:
        print(k)
        break
else:
    print(-1)
```