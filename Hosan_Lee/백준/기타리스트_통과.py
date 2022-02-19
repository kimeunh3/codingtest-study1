length, start, max = map(int, input().split())
volume = list(map(int, input().split()))
dp = [[0] * (max+1) for _ in range(length+1)]
dp[0][start]= 1

for i in range(1, length+1):
	for j in range(max+1):
		if dp[i-1][j] == 0 :
			continue
		if j - volume[i-1]>=0:
			dp[i][j- volume[i-1]] = 1
		if j + volume[i-1]<=max:
			dp[i][j+ volume[i-1]] = 1
result = -1
for i in range(max,-1,-1):
	if dp[length][i] ==1:
		result= i
		break
print(result)