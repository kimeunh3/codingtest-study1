## 백준 2504번

### 알고리즘

- **stack 자료 구조 사용**

### 코드 구현

사용 언어 : **파이썬**

```python
# 방법1
bracket = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(bracket)):

    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if bracket[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if bracket[i-1] == "[":
            answer += tmp
        stack.pop()
        tmp //= 3
if stack:
    print(0)
else:
    print(answer)

```

```python
# 방법2
bracket = list(input())

stack = []

for i in range(len(bracket)):
    # (이나 [이면 스택에 추가
    if bracket[i] == '(' or bracket[i] == '[':
        stack.append(bracket[i])
    elif bracket[i] == ')':
        # 스택이 비어있는데 )이 들어왔거나 이전 값이 [이라면 올바른 괄호열이 아니므로 스택을 비워주고 for루프 나감
        if not stack or stack[-1] == "[":
            stack = []
            break
        # 만약에 stack[-1]이 (이면 ()=>2 이므로 stack[-1]=2로 초기화
        if stack[-1] == '(':
            stack[-1] = 2
        # stack[-1]이 숫자라면
        else:
            temp = 0
            # (를 만날 때까지 계산
            for idx in range(len(stack)-1, -1, -1):
                if stack[idx] == '(':
                    stack[-1] = temp*2
                    break
                # * 예외처리를 또 해줘야 함 *
                # (를 만나지 않았는데 숫자들 사이에 [가 끼어있으면 잘못된 문자열이므로 스택 비워주고 빠져나감
                elif stack[idx] == '[':
                    stack = []
                    break
                else:
                    temp += stack[-1]
                    stack.pop()
            if not stack:
                break
    # )를 만났을 때와 같은 방식으로 ]를 만났을 때 처리
    else:
        if not stack or stack[-1] == "(":
            stack = []
            break
        if stack[-1] == "[":
            stack[-1] = 3
        else:
            temp = 0

            for idx in range(len(stack)-1, -1, -1):
                if stack[idx] == '[':
                    stack[-1] = temp*3
                    break
                elif stack[idx] == '(':
                    stack = []
                    break
                else:
                    temp += stack[-1]
                    stack.pop()
            if not stack:
                break

# 예외처리를 모두 했음에도 불구하고 (나 [가 남아있는 경우가 있음( ex. (()()[] )
# 이런 경우 sum(stack)을 해주면 typeerror가 발생하므로 str이 있을 경우 print(0)처리를 해줌
# stack안의 값이 없거나 숫자만 있는 경우 sum(stack)을 해주면 됨
for i in stack:
    if type(i) is str:
        print(0)
        break
else:
    print(sum(stack))
```
