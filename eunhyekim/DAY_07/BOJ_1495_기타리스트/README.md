## 풀이

동적계획법으로 풀었습니다.

cache는 다음과 같습니다:

```
cache[i][j] = i번째 곡을 j 볼륨으로 연주 가능한지 여부
cache[1][3] = 1 이라면 첫번째 곡을 볼륨 3으로 연주가 가능하다는 뜻
```

각각 이전 곡의 가능한 볼륨을 찾아준 뒤, 볼륨을 줄여주었을 때 0보다 크거나 같고, 볼륨을 더해주었을 때 M보다 작거나 같다면 해당 cache에 1을 저장해줍니다.  

모든 cache를 다 돌아준 뒤 마지막 곡을 뒤에서부터 돌아주면서 가능한 볼륨을 찾으면 바로 print 해줍니다. 찾지 못했다면 -1을 출력해줍니다.  

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
