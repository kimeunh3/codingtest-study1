bracket = list(input())

stack = []

for i in range(len(bracket)):
    if bracket[i] == '(' or bracket[i] == '[':
        stack.append(bracket[i])
    elif bracket[i] == ')':
        if not stack or stack[-1] == "[":
            stack = []
            break
        if stack[-1] == '(':
            stack[-1] = 2
        else:
            temp = 0
            for idx in range(len(stack)-1, -1, -1):
                if stack[idx] == '(':
                    stack[-1] = temp*2
                    break
                elif stack[idx] == '[':
                    stack = []
                    break
                else:
                    temp += stack[-1]
                    stack.pop()
            if not stack:
                break
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
if not stack:
    print(0)
else:
    for i in stack:
        if type(i) is str:
            print(0)
            break
    else:
        print(sum(stack))
