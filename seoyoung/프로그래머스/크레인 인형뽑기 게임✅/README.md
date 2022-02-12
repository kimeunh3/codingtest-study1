## 프로그래머스 크레인 인형뽑기 게임

### 풀이 과정

```txt
✅ 파이썬은 stack 역할을 하는 리스트가 있어 stack을 따로 구현해주지 않아도 됨
✅ stack 안에 아무것도 들어있지 않은 경우 원소에 접근하려고 하면 오류가 발생하므로 그 부분에 유의해서 풀어주면 됨
```

### 코드 구현

사용 언어 : **파이썬**

```python
def solution(board, moves):
    answer = 0
    stack = []

    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                if len(stack) >= 1 and stack[len(stack)-1] == board[i][move-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[i][move-1])
                board[i][move-1] = 0
                break

    return answer
```
