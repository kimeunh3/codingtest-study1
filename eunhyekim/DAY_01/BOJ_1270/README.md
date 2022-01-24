## 풀이  

Counter를 사용하여 가장 많은 수의 troop이 절반을 초과하는지 확인해주었고 그러지 않으면 "SYJKGW"를 출력해주었습니다.

## 코드  
```python
from collections import Counter

N = int(input())
for _ in range(N):
    troops = list(map(int, input().split()))
    num_troop, troops = troops[0], troops[1:]
    max_troop = Counter(troops).most_common(1)[0]
    result = max_troop[0] if max_troop[1] > num_troop // 2 else "SYJKGW"
    print(result)
```