
N = int(input())
Day, Money = [0 for i in range(N+1)], [0 for i in range(N+1)]
for i in range(N):
    D,M = map(int, input().split())
    Day[i] = D
    Money[i] = M

dp =[0 for i in range(N+1)]

for i in range(len(Day)-2, -1, -1):
    if Day[i]+i <= N:
        dp[i] = max(Money[i] + dp[i + Day[i]], dp[i+1])
    else:                 # 날짜를 초과할 경우.
        dp[i] = dp[i+1]
print(dp[0])