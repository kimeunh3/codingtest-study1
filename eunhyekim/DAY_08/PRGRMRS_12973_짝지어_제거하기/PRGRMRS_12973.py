def solution(s):
    idx = 0
    while len(s) > 0:
        if idx == len(s):
            return 0
        if idx+1 < len(s) and s[idx+1] == s[idx]:
            num = 2
            for i in range(idx+2, len(s)):
                if s[i] != s[idx]:
                    break
                num += 1
            num = num-1 if num % 2 else num
            s = s[:idx] + s[idx+num:]
            if len(s) == 0: return 1
            idx = idx-1 if idx > 0 else idx
            continue
        idx += 1
        
def solution(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    
    return 0 if stack else 1