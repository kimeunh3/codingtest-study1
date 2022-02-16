## 백준 14501번

### 알고리즘

- **다이나믹 프로그래밍**

### 코드 구현

사용 언어 : **파이썬**

```python
N = int(input())
consult = []

for i in range(N):
    consult.append(list(map(int, input().split())))

dp = [0 for i in range(N+1)]

# N일부터 거꾸로 탐색해야 함
# ex. 1일 ~ 3일 10만원 / 2일 ~ 4일 20만원 이라면 후자를 선택해야 함.
# 이 경우를 처리하기 위해서 뒤에서부터 탐색하며 다이나믹 프로그래밍하며 최대 이익을 dp[i]에 저장하여 dp[i-1]에서 사용하도록 함
for i in range(N-1, -1, -1):
    # N일을 넘어서는 일은 할 수 없기 때문에 현재 일수에서 최대 이익은 dp[i+1]
    if i+consult[i][0] > N:
        dp[i] = dp[i+1]
    # 할 수 없는 일이 아니라면
    else:
        # 현재까지의 최대 이익(dp[i+1])
        # 현재 할 수 있는 상담 금액(consult[i][1])+현재 상담을 마치고 할 수 있는 시점에서의 최대 이익(dp[i+consult[i][0]])
        # 을 비교하여 더 큰 수를 현재 시점까지의 최대 이익으로 저장 dp[i]
        dp[i] = max(dp[i+1], consult[i][1]+dp[i+consult[i][0]])

print(dp[0])
```
