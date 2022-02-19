N = int(input())
consult = []

for i in range(N):
    consult.append(list(map(int, input().split())))

dp = [0 for i in range(N+1)]

for i in range(N-1, -1, -1):
    if i+consult[i][0] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], consult[i][1]+dp[i+consult[i][0]])

print(dp[0])
