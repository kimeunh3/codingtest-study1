## 풀이  

그리디 알고리즘을 이용해 풀어주었습니다.  

timeline을 끝나는 시간이 빠른순서로 정렬해주었습니다. 끝나는 시간이 같다면 시작하는 시간이 빠른 순서로 정렬되게끔 두번째 key로 넣어주었습니다.  

그런 뒤 가장 끝나는 시간이 빠른 미팅부터 진행하며 그 뒤로 가능한 미팅을 찾아 meetings의 수를 update해주었습니다.  

## 코드  
```python
import sys
from collections import deque

iuput = sys.stdin.readline

N = int(input())
timeline = []
for _ in range(N):
    timeline.append(tuple(map(int, input().split())))
timeline = deque(sorted(timeline, key=lambda x: (x[1], x[0])))
prev_end = 0
meetings = 0
while timeline:
    start, end = timeline.popleft()
    if prev_end <= start:
        meetings += 1
        prev_end = end
print(meetings)
```