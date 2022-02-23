def solution(s):
    answer = -1

    stack = []

    for i in s:
        if len(stack) == 0 or stack[-1] != i:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop()
    else:
        if len(stack) != 0:
            answer = 0
        else:
            answer = 1
    return answer
