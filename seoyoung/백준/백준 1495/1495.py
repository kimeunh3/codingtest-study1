N, S, M = map(int, input().split())
volume = list(map(int, input().split()))
dp = [[] for i in range(N+1)]
dp[0].append(S)

for i in range(1, N+1):
    for j in range(len(dp[i-1])):
        maxVol = dp[i-1][j]+volume[i-1]
        minVol = dp[i-1][j]-volume[i-1]
        if maxVol <= M and maxVol not in dp[i]:
            dp[i].append(maxVol)
        if minVol >= 0 and minVol not in dp[i]:
            dp[i].append(minVol)

    if len(dp[i]) == 0:
        print(-1)
        break
else:
    print(max(dp[N]))
