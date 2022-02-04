## 풀이

각자 width와 height의 list를 만들어준 뒤 width에는 size값의 둘 중 작은 사이즈를, height에는 큰 사이즈를 넣어준 뒤 마지막에는 각각의 list에서 max값을 구해 서로 곱한 값을 return해주었습니다.

## 코드
```python
def solution(sizes):
    width = []
    height = []
    for size in sizes:
        if size[0] < size[1]:
            width.append(size[0])
            height.append(size[1])
        else:
            width.append(size[1])
            height.append(size[0])
    return max(width)*max(height)
```