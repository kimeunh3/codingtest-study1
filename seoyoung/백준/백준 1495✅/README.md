## 백준 1495번 기타리스트

### 알고리즘

- **다이나믹 프로그래밍**

### 코드 구현

사용 언어 : **파이썬**

```python
# N=곡 개수, S=시작 볼륨, M=최대 볼륨
N, S, M = map(int, input().split())
volume = list(map(int, input().split()))
dp = [[] for i in range(N+1)]
dp[0].append(S)

for i in range(1, N+1):
    for j in range(len(dp[i-1])):
        maxVol = dp[i-1][j]+volume[i-1]
        minVol = dp[i-1][j]-volume[i-1]
        # dp[i]에 포함되어 있지 않은 경우에만 볼륨을 추가해줘야함 안그러면 메모리 초과 오류남...
        if maxVol <= M and maxVol not in dp[i]:
            dp[i].append(maxVol)
        if minVol >= 0 and minVol not in dp[i]:
            dp[i].append(minVol)
    # 볼륨 조절 시 범위를 벗어난 경우(0보다 작거나 M보다 큰 경우) = dp[i]가 빈 배열
    if len(dp[i]) == 0:
        print(-1)
        break
# break문 써서 빠져나오지 않은 경우 끝까지 볼륨 조절이 가능하다는 것이니까 배열 마지막 값의 최댓값 출력
else:
    print(max(dp[N]))

```
