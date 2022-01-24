## 백준 1024번 수열의 합

### 문제 설명

- N : 수열의 합
- L : 수열의 최소 길이(2<=N<=100)
- 합이 N이고 길이가 적어도 N인 음이 아닌 정수 리스트 구하기

### 풀이 과정

```txt
✅ 수열의 시작점을 s라고 하면,
➡️ N=s+(s+1)+...+(s+L-1)
➡️ N=s*L+(1부터 L-1까지의 합)
➡️ N=s*L+L*(L-1)/2
➡️ s=N/L-(L-1)/2
✅ 위의 수식을 활용하여 L부터 100까지 for문을 돌면서 s가 양의 정수인 경우 for문을 빠져나가고 수열을 출력하도록 함
```

### 코드 구현

사용 언어 : **파이썬**

```python
N, L = map(int, input().split())
# 최종 수열의 시작점을 저장할 변수
start = -1
# 최종 수열의 길이를 저장할 변수
len = L

for i in range(L, 101):
    s = N/i - (i-1)/2
    # s가 양의 정수인 경우
    if s == int(s) and s >= 0:
        start = s
        len = i
        break

if start == -1:
    print(-1)
else:
    for i in range(len):
        # start는 소수형태로 저장되어 있어서 정수 모양으로 바꿔줘야 함
        print(int(start)+i, end=' ')
```
