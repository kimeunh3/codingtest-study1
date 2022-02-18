N = int(input())
T = [0 for i in range(N + 1)]
P = [0 for j in range(N + 1)]

for i in range(N):
    time, price = map(int, input().split())
    T[i] = time
    P[i] = price

# dp[operation_list]는 i번째 날까지 일을 했을 때, 최대값을 저장한다!
dp = [0 for i in range(N + 1)]

for i in range(N - 1, -1, -1):  # 시간을 초과하면 상담을 하지 않기 때문에 역순으로 진행
    if T[i] + i <= N:  # 날짜를 초과하지 않을 경우.
        dp[i] = max(P[i] + dp[i + T[i]], dp[i + 1])

    else:  # 날짜를 초과할 경우.
        dp[i] = dp[i + 1]

print(dp[0])

# 각 날짜에 최대를 dp에 저장한 후 operation_list 날에 일을 하는 기간인 T[operation_list]를 더한값이 N을 넘으면 회사에 없기 때문에 불가
# 넘는다면 그 날일을 건너뛰고 그 전날로 돌아가 반복.
# 넘지 않는다면 max(P[operation_list] + dp[operation_list + T[operation_list]], dp[operation_list + 1]) 를 통해 현재 총액 + 상담금액과 그 전에 저장된 dp 값을 비교해서
# 더 큰 값을 dp에 저장한다.

