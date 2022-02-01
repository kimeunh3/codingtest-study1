## 풀이  



## 코드  
```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)
lo, hi = 0, trees[0]-1
height = 0
while lo <= hi:
    mid = (lo + hi) // 2
    cut = 0
    for tree in trees:
        if tree < mid:
            break
        if cut >= M:
            break
        cut += tree - mid
    if cut >= M:
        lo = mid + 1
        height = max(height, mid)
    else:
        hi = mid - 1
print(height)
```