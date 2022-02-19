## 풀이  



## 코드  
```python

N, S, M = map(int, input().split())
V = list(map(int, input().split()))
cache = [ [0, 0] for _ in range(N) ]

def plus_check(i, j):
    return cache[i-1][j]+V[i] if 0 <= cache[i-1][j]+V[i] <= M else -1

def minus_check(i, j):
    return cache[i-1][j]-V[i] if 0 <= cache[i-1][j]+V[i] else -1

# cache[i][0] = P + V[i]
# cache[i][1] = P - V[i]
cache[0][0] = S+V[0] if S+V[0] <= M else S
cache[0][1] = S-V[0] if S-V[0] >= 0 else S
for i in range(1, N):
    cache[i][0] = max(cache[i-1][0]+V[i], cache[i-1][1]+V[i])
    cache[i][1] = max(cache[i-1][0]-V[i], cache[i-1][1]-V[i])
    if cache[i][0] > M or cache[i][1] < 0:
        print(-1)
        break
else:
    print(max(cache[N-1]))
```