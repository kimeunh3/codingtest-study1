## 프로그래머스 타겟 넘버

### 알고리즘

- DFS

### 풀이 과정

```txt
✅ 베열의 원소 앞에 +혹은 -를 끼워넣어서 나올 수 있는 값 중 target과 같은 것을 구하는 문제이기 때문에 앞에서 순차적으로 계산해온 결과들에 현재 값을 더하거나 빼주면 됨
✅ depth가 numbers의 길이와 같으면 이미 계산을 마친 결과들이므로 target과 비교해주면 됨.
✅ depth가 numbers의 길이보다 작으면 재귀함수로 지금까지 연산해온 결과(number)에 현재 깊이의 배열 원소(numbers[depth])를 더하거나 뺀 결과를 인자로 넘겨줌
```

### 코드 구현

사용 언어 : **파이썬**

```python
answer = 0

def dfs(depth, number, numbers, target):
    global answer
    if depth == len(numbers):
        if number == target:
            answer += 1
        return

    dfs(depth+1, number+numbers[depth], numbers, target)
    dfs(depth+1, number-numbers[depth], numbers, target)


def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)
    return answer
```
