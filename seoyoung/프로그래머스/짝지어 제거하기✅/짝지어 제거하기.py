def solution(s):
    answer = 0
    stack = []

    for char in s:
        if len(stack) == 0 or stack[-1] != char:
            stack.append(char)
        else:
            stack.pop()

    if not stack:
        answer = 1

    return answer
