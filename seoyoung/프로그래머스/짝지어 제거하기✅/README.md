## 프로그래머스 짝지어 제거하기

### 코드 구현

사용 언어 : **파이썬**

```python
def solution(s):
    answer = 0
    # 스택을 사용하여 문자가 연속되면 삭제하는 형태로 문제 해결
    stack = []

    for char in s:
        # 스택이 비어있거나 스택의 top에 있는 값이 현재 문자열과 같지 않으면 스택에 char 삽입
        if len(stack) == 0 or stack[-1] != char:
            stack.append(char)
        # stack[-1]==char이라면 stack[-1]값 삭제
        else:
            stack.pop()

    # stack에 문자가 남아있지 않다면 = 짝지어 모든 문자를 제거 가능 => answer=1
    # stack에 문자가 남아있다면 = 모든 문자 제거 x => answer=0
    if not stack:
        answer = 1

    return answer


```
