## 백준 1011번 Fly me to the Alpha Centauri

### 풀이 과정

```txt
✅ 공간 이동 반복 횟수가 repeat이라고 할 때, repeat*(repeat+1)+1 지점에서 반복횟수 +1
✅ 이동거리가 repeat**2 보다 작으면 공간이동 작동 횟수는 repeat*2-1,  repeat**2 보다 크면 repeat*2 이다.

```

### 코드 구현

사용 언어 : **파이썬**

```python
T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    distance = y-x
    repeat = 1

    while True:
        if distance <= repeat*(repeat+1):
            break
        repeat += 1

    if distance > repeat**2:
        print(repeat*2)
    else:
        print(repeat*2-1)
```
