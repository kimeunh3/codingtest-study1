## 프로그래머스 N으로 표현

### 풀이 과정

```txt
✅ dp배열 내에 set를 사용해서 N을 i번 사용해서 만들 수 있는 연산결과가 중복되는 것이 없도록 함
✅ 동적 프로그래밍 이용
➡️ N을 한 번 사용해서 만들 수 있는 수는 N => dp[1]={N}
➡️ N을 두번 사용해서 만들 수 있는 수는 NN, N+N, N-N, N*N, N/N => dp[2]={NN, N+N, N-N, N*N, N/N} => NN을 미리 넣어준다고 가정하면 dp[1]의 수를 사칙연산한 결과 => dp[2]={NN, dp[1]+dp[1],dp[1]-dp[1]..}
➡️ N을 세번 사용해서 만들 수 있는 수는 NNN, (dp[1],dp[2] 연산), (dp[2],dp[1] 연산)
➡️ 즉, N을 i번 사용해서 만들 수 있는 수는 int(str(N)*i), (dp[1],dp[i-1] 연산), (dp[2],dp[i-2]), .. (dp[i-1],dp[1] 연산)
➡️ i번 사용해서 만들 수 있는 수를 모두 구한 다음 dp[i]에 number가 포함되어 있다면 i를 리턴, 모든 경우의 수를 다 구했는데도 number가 배열에 존재하지 않는다면 -1을 리턴하도록 함
```

### 코드 구현

사용 언어 : **파이썬**

```python
def solution(N, number):
    dp=[None]+[{int(str(N)*i)} for i in range(1,9)]

    for i in range(1,9):
        for j in range(1,i):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1+op2)
                    dp[i].add(op1-op2)
                    dp[i].add(op1*op2)
                    if op2!=0:
                        dp[i].add(op1//op2)

        if number in dp[i]:
            return i

    return -1
```
