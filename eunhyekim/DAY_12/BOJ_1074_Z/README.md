## 풀이

분할정복으로 풀어주었습니다.

현재 y+n, x+n이 각각 r, c보다 클 경우에는 분할을, 그렇지 않을 때는 그 크기의 사각형 만큼 숫자를 늘려주었습니다.

## 코드

```python
N, r, c = map(int, input().split())

cnt = 0
def divide(n, y, x):
    global cnt
    if y == r and x == c:
        print(cnt)
        exit(0)
    if n == 1:
        cnt += 1
    else:
        if y+n > r and x+n > c:
            n //= 2
            divide(n, y, x)
            divide(n, y, x+n)
            divide(n, y+n, x)
            divide(n, y+n, x+n)
        else:
            cnt += n*n # 사각형의 크기만큼 늘려주기

divide(2**N, 0, 0)
```
