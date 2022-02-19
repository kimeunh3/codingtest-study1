## 풀이  



## 코드  
```python
import sys

input = sys.stdin.readline

T = int(input())
status = [0, 1]

def move(action, x, y):
    global status

    if action == "F":
        return x+status[0], y+status[1]
    elif action == "B":
        return x-status[0], y-status[1]
    elif action == "L":
        if status[1]:
            status = [-status[1], -status[0]]
        else:
            status = [status[1], status[0]]
        return x, y
    else:
        if status[0]:
            status = [-status[1], -status[0]]
        else:
            status = [status[1], status[0]]
        return x, y

cases = [input() for _ in range(T)]
for case in cases:
    x, y = 0, 0
    minX, maxX, minY, maxY = 0, 0, 0, 0 
    for action in case:
        x, y = move(action, x, y) 
        minX, maxX, minY, maxY = min(minX, x), max(maxX, x), min(minY, y), max(maxY, y)
        # print(x, y, status)
    print((maxX-minX)*(maxY-minY))
```