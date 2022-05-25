## 풀이  

y지점에 도착하기 바로 직전의 이동거리를 반드시 1광년으로 하려 하기 때문에 N이 주어진다면 다음과 같이 이동해야 최소 거리가 됩니다.

```
보여지는 숫자는 작동 횟수 당 이동하는 거리
1 2 3 ... N/2-1 N/2 N/2-1 ... 3 2 1
여기서 N은 작동 횟수
```

양방향에서 일정하게 늘어나는 수열로 이루어져 있기 때문에 양방향에서 같은 값을 두 번 더해주기 위해
늘어나는 수를 1이 아닌 0.5로 한 뒤, int casting을 활용하여 내림한 값을 누적해서 구해주었습니다.

```
while 구문 작동 예:
  x, y = 1, 5
  dist = 4
  increase_repeat = 0.5
  activation = 0
  check_dist = 0

  첫 번째:
    check_dist = 0
    dist = 4
    increase_repeat = 0.5 -> 1.0
    check_dist = 0 -> 1
    activation = 0 -> 1
  두 번째:
    check_dist = 1
    dist = 4
    increase_repeat = 1.0 -> 1.5
    check_dist = 1 -> 2
    activation = 1 -> 2
  세 번째:
    check_dist = 2
    dist = 4
    increase_repeat = 1.5 -> 2.0
    check_dist = 2 -> 4
    activation = 2 -> 3
  check_dist = 4
  dist = 4
  activation = 3
```

## 코드  
```python
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    dist = y - x # 목적지까지의 거리
    increase_repeat = 0.5 # 두 번에 걸쳐 늘어나기 때문에 반복 횟수가 0.5씩 늘어난다.
    activation = 0 # 작동 횟수
    check_dist = 0 # dist와 현재 이동 거리를 비교해주기 위한 거리
    
    while check_dist < dist:
        increase_repeat += 0.5
        check_dist += int(increase_repeat)
        activation += 1
    print(activation)
```
