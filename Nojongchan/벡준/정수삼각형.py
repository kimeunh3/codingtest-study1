import sys
N = int(sys.stdin.readline())
P =[list(map(int, sys.stdin.readline().split())) for i in range(N)] # 문제의 삼각형

dp = [[0] * i for i in range(1, N + 1)] # 삼각형 위의 원소와 아래의 원소를 더한 값을 입력할 새로운 삼각형.  
dp[0][0] = P[0][0]  

for i in range(1, N):  # 삼각형의 크기 만큼 반복
    for j in range(i+1):
        if j == 0:  # 삼각형 줄의 맨 왼쪽 
            dp[i][j] = dp[i-1][j] + P[i][j]
        elif j == i:  # 삼각형 줄의 맨 오른쪽 
            dp[i][j] = dp[i-1][j-1] + P[i][j]
        else:  # 삼각형 줄 가운데의 값을 구할 떄,  경우의 수가 두가지 이므로 둘중의 최댓값을 구해서 대입.
            dp[i][j] = max(dp[i-1][j-1] + P[i][j], dp[i - 1][j] + P[i][j])

print(dp)
print(max(dp[-1]))
