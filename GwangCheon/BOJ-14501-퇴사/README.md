---

### 📔 문제 설명

![](https://images.velog.io/images/soshin_dev/post/e957e86c-c8a4-44f9-94a4-daff79c76f74/image.png)

[문제 풀러 가기](https://www.acmicpc.net/problem/14501)

### 🧰 변수 설명

- **N**
    - 타입 : 정수
    - 저장 데이터 : 일 수 입력
- **dp**
    - 타입 : 리스트
    - 저장 데이터 : 각 날짜마다의 최대값을 저장
- **T**
    - 타입 : 리스트
    - 저장 데이터 : 상담 소요 시간 저장
- **P**
    - 타입 : 리스트
    - 저장 데이터 : 상담 금액 저장


### 🖨풀이 과정

```txt
1. 일 수를 입력 받는다 [N]
2. 시간과 금액을 저장할 리스트를 초기화 해준다. [T, P]
3. 반복문을 통해 N 만큼 반복하며 각 상담마다의 소요 시간과 금액을 입력받는다.
4. dp를 N+1 크기 만큼 초기화 해준다. (회사를 N+1 일에 나가기 때문에)
5. 시간을 초과하면 회사에 있지 않기 때문에 역순으로 반복문을 돈다.
6. 현재 날짜와 상담 소요시간을 더 한 값이 N보다 작다면 큰 값을 비교하여 큰 값을 dp에 넣는다.
7. 만약 현재 날짜와 상담 소요시간을 더한 값이 N보다 크면 dp[i] = dp[i+1] 을 해준다.
8. 마지막에 dp[0]에는 반복문을 종료 후 가장 큰 값이 들어있기 때문에 dp[0]를 출력해준다.
```
```python
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
```
시간 : **68ms**
