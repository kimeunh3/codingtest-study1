## 풀이

DFS를 이용하여 풀어주었습니다.

dfs 함수를 만들어주었고 parameter는 다음과 같습니다.
- cnt: 이떄까지 연산한 숫자의 개수
- res: 이때까지 연산하여 나온 값
- add: 남은 덧셈의 개수
- sub: 남은 뺄셈의 개수
- mul: 남은 곱셈의 개수
- div: 남은 나눗셈의 개수

해당 연산이 가능할 경우에만 연산을 해주며 모든 경우의 수를 돌아줍니다. 돌아주며 최솟값과 최댓값을 계속 업데이트해주며 값을 구해줍니다.  

## 코드

```python
import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
min_n, max_n = 1e9, -1e9

def dfs(cnt, res, add, sub, mul, div): 
    global min_n, max_n
    if cnt == N: 
        max_n = max(res, max_n) 
        min_n = min(res, min_n) 
        return 
    if add: 
        dfs(cnt+1, res+nums[cnt], add-1, sub, mul, div) 
    if sub: 
        dfs(cnt+1, res-nums[cnt], add, sub-1, mul, div) 
    if mul: 
        dfs(cnt+1, res*nums[cnt], add, sub, mul-1, div) 
    if div: 
        dfs(cnt+1, int(res/nums[cnt]), add, sub, mul, div-1) 
        

dfs(1, nums[0], add, sub, mul, div) 
print(max_n, min_n, sep="\n")
```
