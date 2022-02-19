import sys

N, S, M = map(int, sys.stdin.readline().split())
V = list(map(int, sys.stdin.readline().split()))
# 곡의 개수 N
# 시작 볼륨 S
# 최대 불륨 M
# 불륨 리스트 V

dp = [[0]*(M+1) for i in range(N+1)]

dp[0][S] = 1

for n in range(1, N + 1):
    for m in range(0, M + 1):
        if dp[n-1][m] == 0:
            continue
        if m - V[n-1] >= 0:
            dp[n][m - V[n-1]] = 1
        if m + V[n-1] <= M:
            dp[n][m + V[n-1]] = 1

result = -1

for i in range(M, -1, -1):
    if dp[N][i] == 1:
        result = i
        break

print(result)