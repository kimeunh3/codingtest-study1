## 백준 14888번 연산자 끼워넣기

### 알고리즘

- **DFS**

### 코드 구현

사용 언어 : **파이썬**

```python
N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
maxNum = -1e9
minNum = 1e9

# 숫자는 그대로 있고, 모든 경우의 연산자를 끼워넣기 위해 dfs 사용
# depth가 N이면 연산을 완료했다는 소리이기 때문에 특정 연산자 조합에 의해 계산된 최대값, 최소값과 현재 num을 비교하여 결정
# 각 연산자(+,-,*,/)의 개수를 인자로 넘겨줘서 다음 dfs에도 연산자 개수들이 반영될 수 있도록 함
def dfs(depth, num, plus, minus, mul, div):
    global maxNum, minNum
    if depth == N:
        maxNum = max(num, maxNum)
        minNum = min(num, minNum)
        return

    if plus:
        dfs(depth+1, num+nums[depth], plus-1, minus, mul, div)
    if minus:
        dfs(depth+1, num-nums[depth], plus, minus-1, mul, div)
    if mul:
        dfs(depth+1, num*nums[depth], plus, minus, mul-1, div)
    if div:
        #그런데 여기 num//nums[depth] 가 안되는 이유가 궁금함...
        dfs(depth+1, int(num/nums[depth]), plus, minus, mul, div-1)


dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])
print(maxNum)
print(minNum)
```
