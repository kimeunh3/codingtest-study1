## 풀이  

동적계획법으로 풀었습니다. 
cache는 다음과 같습니다.  
```
cache[i][0] = i+1번째 날을 포함하지 않는 경우
cache[i][1] = i+1번째 날을 포함하는 경우
```

for loop을 처음부터 N길이 까지 돌려준 뒤 퇴사 전까지 상담이 끝나는 경우에만 돌려주었습니다.  
cache\[i\]\[1\]에 i+1번째 날짜의 금액을 더해주고, i+1번째를 포함할 수 있는 날짜들(i+1번째 상담이 끝난 뒤의 날짜들)의 현재 값과, i+1번째의 값 중 큰 값으로 update해주었습니다.  

마지막에는 cache에 있는 수들 중 가장 큰 값을 찾아 return해줍니다.  
## 코드  
```python
import sys
input = sys.stdin.readline

N = int(input())
schedule = [ list(map(int, input().split())) for _ in range(N) ]
cache = [[0, 0] for _ in range(N)]

for i in range(N):
    if i + schedule[i][0]-1 >= N:
        continue
    cache[i][1] += schedule[i][1]
    for j in range(i+1, N):
        if j >= i + schedule[i][0]:
            cache[j][0] = max(cache[i][0], cache[i][1], cache[j][0])
            cache[j][1] = max(cache[i][0], cache[i][1], cache[j][1])

print(max(map(max, cache)))

```