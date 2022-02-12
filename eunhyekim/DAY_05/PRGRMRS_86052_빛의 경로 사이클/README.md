## 풀이

각각 turnRight, turnLeft, goStraight 함수는 빛이 d방향에서 들어왔을 때 가야하는 좌표 y, x와 들어가는 좌표를 기준으로 들어가는 방향 d를 return해줍니다.  

move함수는 주어진 ch에 따라 판단하여 위의 함수를 호출합니다.  

visited는 각 좌표의 상하좌우의 경로에서 들어온적이 있는지 확인하는 3차원 list입니다.  

빛이 격자의 끝을 넘어갈 경우, 반대쪽 끝으로 다시 돌아오기 때문에 모든 경로는 cycle을 가지게 됩니다.  

여기서 하나의 cycle은 모든 좌표를 방문할 필요없이, 시작좌표에서 나간 방향으로 다시 나가게 된다면 cycle이 됩니다.  

예를 들면, ["S", "S"] 라는 격자의 경우, 아래와 같은 6개의 cycle들이 있습니다.  
<img src="https://user-images.githubusercontent.com/59808674/153693159-3701e8cc-e18a-4adf-a3bc-7a44a60b6d6e.png" width="300">
<img src="https://user-images.githubusercontent.com/59808674/153693161-ff50cc3f-3e28-47b4-82c5-14d87637e6c4.png" width="300"><br>

----

<img src="https://user-images.githubusercontent.com/59808674/153693162-ec4406f7-5e80-439b-b5ed-89a9cd04f85e.png" width="300"> 
<img src="https://user-images.githubusercontent.com/59808674/153693163-4a6230bc-4a26-43ef-be03-24e842a004d7.png" width="300"><br>

----

<img src="https://user-images.githubusercontent.com/59808674/153693164-15284cd3-0863-4401-ae21-6bc8be9f6285.png" height="300">
<img src="https://user-images.githubusercontent.com/59808674/153693165-c031e08b-ecd0-44ef-ac0a-ce72fd039c73.png" height="300">

그렇기 때문에 이미 방문했던 경로라면, 중복된 cycle을 다시 세어주는 것이기 때문에  
각각의 좌표에서 방문하지 않았던 경로만 방문하면서, 그 경로를 포함한 cycle의 길이를 구해 answer list에 넣어주면 됩니다.  

마지막에는 answer를 오름차순으로 정렬하여 return해줍니다.  

## 코드
```python
# 상: 0, 하: 1, 좌: 2, 우: 3
def turnRight(grid, d, y, x):
    nd, ny, nx = 0, 0, 0
    lenY, lenX = len(grid), len(grid[0])
    if d == 0:
        ny = y
        nx = (lenX + x - 1) % lenX
        nd = 3
    elif d == 1:
        ny = y
        nx = (x + 1) % lenX
        nd = 2
    elif d == 2:
        ny = (y + 1) % lenY
        nx = x
        nd = 0
    else:
        ny = (lenY + y - 1) % lenY
        nx = x
        nd = 1

    return nd, ny, nx
    
def turnLeft(grid, d, y, x):
    nd, ny, nx = 0, 0, 0
    lenY, lenX = len(grid), len(grid[0])
    if d == 0:
        ny = y
        nx = (x + 1) % lenX
        nd = 2
    elif d == 1:
        ny = y
        nx = (lenX + x - 1) % lenX
        nd = 3
    elif d == 2:
        ny = (lenY + y - 1) % lenY
        nx = x
        nd = 1
    else:
        ny = (y + 1) % lenY
        nx = x
        nd = 0

    return nd, ny, nx

def goStraight(grid, d, y, x):
    nd, ny, nx = 0, 0, 0
    lenY, lenX = len(grid), len(grid[0])
    if d == 0:
        ny = (y + 1) % lenY
        nx = x
        nd = 0
    elif d == 1:
        ny = (lenY + y - 1) % lenY
        nx = x
        nd = 1
    elif d == 2:
        ny = y
        nx = (x + 1) % lenX
        nd = 2
    else:
        ny = y
        nx = (lenX + x - 1) % lenX
        nd = 3

    return nd, ny, nx

def move(ch, grid, d, y, x):
    if ch == "S":
        return goStraight(grid, d, y, x)
    elif ch == "R":
        return turnRight(grid, d, y, x)
    else:
        return turnLeft(grid, d, y, x)
        

def solution(grid):
    answer = []
    visited = [ [ [0, 0, 0, 0] for _ in range(len(grid[0])) ] for _ in range(len(grid)) ]
    total_path = len(grid)*len(grid[0])*4
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(4):
                if visited[i][j][k]:
                    continue
                cnt = 0
                d, y, x = k, i, j
                while True:
                    if visited[y][x][d]:
                        if y == i and x == j:
                            answer.append(cnt)
                        break
                    cnt += 1
                    visited[y][x][d] = 1
                    d, y, x = move(grid[y][x], grid, d, y, x)
    answer.sort()
    return answer
```
