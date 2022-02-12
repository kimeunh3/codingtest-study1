import sys
input = sys.stdin.readline
dp = []

N = int(input())
for i in range(N):
    dp.append(list(map(int, input().split())))

for i in range(1, N):
    for j in range(0, i+1):
        if j == 0:
            dp[i][j] += dp[i-1][j]
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[N-1]))
