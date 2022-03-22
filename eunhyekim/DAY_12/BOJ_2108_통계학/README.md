## 풀이

Counter로도 풀어보고 dictionary로도 풀어봤지만 비교했을 때 Counter가 더 빠른 Runtime을 가졌습니다.

## 코드

```python
from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
arr = [ int(input()) for _ in range(N)]
arr.sort()
length = len(arr)
mid = length // 2
cnt = Counter(arr).most_common(2)
mean = round(sum(arr)/length)
median = arr[mid] if length % 2 else (arr[mid]+arr[mid-1]) // 2
mode = sorted(cnt, key=lambda x: x[0])[1][0] if len(cnt) > 1 and cnt[0][1] == cnt[1][1] else cnt[0][0]
range_ = max(arr) - min(arr)

print(mean)
print(median)
print(mode)
print(range_)
```
