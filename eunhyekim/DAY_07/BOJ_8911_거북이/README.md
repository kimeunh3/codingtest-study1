## 풀이

우선 status에 x와 y의 상태를 담아줍니다. status는 거북이가 바라보고 있는 방향을 다음과 같이 알려줍니다.  
```
status = [x, y]

x와 y는 한 눈금 앞으로 (F) 갈 때 더해주는 값이 들어가게 됩니다.
북 = [0, 1]
남 = [0, -1]
동 = [1, 0]
서 = [-1, 0]
```

처음에는 북쪽을 쳐다보고 있는 상태이기 때문에 x는 0, y는 1로 초기화 해줍니다.  

이후로는 명령에 따라 현 좌표값을 바꿔주거나, status를 바꿔주어야 합니다.
- F: 좌표에 status 값을 더해줍니다.  
- B: 좌표에 status 값을 빼줍니다.
- L: status의 x, y 서로의 값을 뒤바꾸어 줍니다. y의 값이 0이 아닐 경우에는(북, 또는 남쪽을 바라보고 있을 때) x와 y를 음수로 바꿔줍니다.  
  - 북 → 서 = [0, 1] → [-1, 0]
  - 남 → 동 = [0, -1] → [1, 0]
  - 동 → 북 = [1, 0] → [0, 1]
  - 서 → 남 = [-1, 0] → [0, -1]
- R: status의 x, y 서로의 값을 뒤바꾸어 줍니다. x의 값이 0이 아닐 경우에는(동, 또는 서쪽을 바라보고 있을 때) x와 y를 음수로 바꿔줍니다.  
  - 북 → 동 = [0, 1] → [1, 0]
  - 남 → 서 = [0, -1] → [-1, 0]
  - 동 → 남 = [1, 0] → [0, -1]
  - 서 → 북 = [-1, 0] → [0, 1]

명령을 수행할 때마다 나오는 좌표값으로 각각 minX, maxX, minY, maxY를 저장해주며 마지막에는 x와 y의 min과 max값으로 직사각형의 넓이를 구해줍니다.  

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
    print((maxX-minX)*(maxY-minY))
```
