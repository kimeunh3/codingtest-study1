## 백준 1011번 Fly me to the Alpha Centauri

### 풀이 과정

```txt


```

### 코드 구현

사용 언어 : **파이썬**

```python
def solution(sizes):
    width, height = 0, 0
    for size in sizes:
        w, h = max(size), min(size)
        if width < w:
            width = w
        if height < h:
            height = h

    return width*height
```
