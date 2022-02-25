## 백준 8911번 거북이

### 알고리즘

- **구현**

### 코드 구현

사용 언어 : **파이썬**

```python
N = int(input())
control = [input() for i in range(N)]

for con in control:
    # 현재 좌표를 표현할 x,y
    x, y = 0, 0
    # x,y좌표들을 넣어줄 set들을 포함하고 있는 배열 point
    point = [{0}, {0}]
    # 현재 방향 표시 (동-0,서-1,남-2,북-3)
    dir = 3
    for c in con:
        # F,B 일 때는 현재 방향을 기준으로 좌표 변화
        if c == 'F':
            if dir == 0: x += 1
            elif dir == 1: x -= 1
            elif dir == 2: y -= 1
            else: y += 1
        elif c == 'B':
            if dir == 0: x -= 1
            elif dir == 1: x += 1
            elif dir == 2: y += 1
            else: y -= 1
        # L,R일 때는 현재 방향을 기준으로 뱡향 변화
        elif c == 'L':
            if dir == 0: dir = 3
            elif dir == 1: dir = 2
            elif dir == 2: dir = 0
            else: dir = 1
        # c=='R'
        else:
            if dir == 0: dir = 2
            elif dir == 1: dir = 3
            elif dir == 2: dir = 1
            else: dir = 0

        # 명령을 내릴 때마다 x,y좌표를 추가
        # set에 더해주기 때문에 중복 없음
        point[0].add(x)
        point[1].add(y)

    # x축 좌표 최대값 - x축 좌표 최소값 = 너비
    # y축 좌표 최대값 - y축 좌표 최소값 = 높이
    # 너비*높이 = 거북이가 지나간 영역을 모두 포함하는 직사각형
    max_x, min_x = max(point[0]), min(point[0])
    max_y, min_y = max(point[1]), min(point[1])

    print((max_x-min_x)*(max_y-min_y))
```
