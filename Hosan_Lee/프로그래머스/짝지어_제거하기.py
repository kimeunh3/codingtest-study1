def solution(s):
    word_stack = []
    for i in s:
        if len(word_stack) == 0:
            word_stack.append(i)
        elif word_stack[-1] == i:
            word_stack.pop()
        else:
            word_stack.append(i)
    if len(word_stack) == 0:
        return 1
    else:
        return 0