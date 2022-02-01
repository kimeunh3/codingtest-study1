import sys
from collections import deque
N = int(sys.stdin.readline())
result = []

for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    result.append((start, end))

result.sort(key=lambda x: (x[1], x[0]))
result = deque(result)

count = 1
end = result[0][1]
result.popleft()

while result:
    if result[0][0] >= end:
        count += 1
        end = result[0][1]
        result.popleft()
    else:
        result.popleft()
        
print(count)