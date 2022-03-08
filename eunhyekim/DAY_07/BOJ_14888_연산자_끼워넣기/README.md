## 풀이  

처음에는 단순 무식하게 backtracking으로 구현해보려 하였으나, 가지치기를 해주지 않아서 시간 초과되었습니다.  

  
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