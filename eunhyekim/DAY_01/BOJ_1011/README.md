## 풀이  

패턴은 찾았으나 제대로 이해하지 못했습니다...ㅎ

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