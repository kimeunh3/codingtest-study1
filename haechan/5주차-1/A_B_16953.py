'''백준 A->B 16953번'''

import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
oper = [True, False] # True: x2, False: +"1"

dq = deque()
dq.append((a, 0)) # a, count

while dq:
    now, cnt = dq.popleft()

    if now > b: # 숫자가 b보다 커질 경우 해당 숫자를 버리기 위해 continue처리
        continue

    for op in oper:
        count = cnt + 1
        if op:
            result = now * 2
        else:
            result = int(str(now) + "1")
        
        if result == b: # 연산결과(a)가 b와 같아진 경우
            print(count+1)
            exit()
        
        dq.append((result, count))

print(-1)