import sys
N = int(sys.stdin.readline())  # 삼각형의 크기 입력
save = [[int(x) for x in sys.stdin.readline().split()] for _ in range(N)]  # 값 입력

dp = [[0] * i for i in range(1, N + 1)]  # 더한 값을 저장하는 DP 리스트
dp[0][0] = save[0][0]  # 첫 번째 값은 더한 값이 아닌 그대로의 값 이므로 save[0][0] 값을 dp[0][0]에 넣어준다.

for i in range(1, N):  # 삼각형의 크기 만큼 반복
    for j in range(i+1):
        if j == 0:  # 왼쪽 값을 더하기
            dp[i][j] = dp[i-1][j] + save[i][j]
        elif j == i:  # 오른쪽 값을 더하기
            dp[i][j] = dp[i-1][j-1] + save[i][j]
        else:  # 가운데 값을 더할 때, 더 큰값에 더해주기 위해 max 로 비교하기
            dp[i][j] = max(dp[i-1][j-1] + save[i][j], dp[i - 1][j] + save[i][j])

print(max(dp[-1]))