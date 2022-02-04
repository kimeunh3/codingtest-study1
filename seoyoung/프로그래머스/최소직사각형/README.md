## 프로그래머스 최소직사각형

### 풀이 과정

```txt
✅ 명함의 크기를 비교하기 쉽게 너비>높이로 통일시켜줘야 함 (높이<너비도 상관없음)
✅ 통일을 시켰으면 너비 중에 가장 큰 값, 높이 중에 가장 큰 값을 지갑의 너비, 높이로 하면 됨
```

### 코드 구현

사용 언어 : **파이썬**

```python
def solution(sizes):
    width, height = 0, 0

    for size in sizes:
        # size 배열의 더 큰 값을 w에 작은 값을 h에 저장
        w, h = max(size), min(size)
        # w중에 가장 큰 값을 지갑의 width로
        if width < w:
            width = w
        # h 중에 가장 큰 값을 지갑의 height로
        if height < h:
            height = h

    return width*height
```
