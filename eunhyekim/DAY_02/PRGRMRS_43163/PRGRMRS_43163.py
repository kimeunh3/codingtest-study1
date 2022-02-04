def valid(begin, target):
    cnt = 0
    for i in range(len(begin)):
        if begin[i] != target[i]:
            cnt += 1
    return cnt == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    stack = []
    n = len(words)
    visited = [0 for i in range(n)]
    answer = 0
    
    for i in range(n):
        if valid(begin, words[i]):
            stack.append(i)
            
    while stack:
        idx = stack.pop()
        word = words[idx]
        visited[idx] = 1
        answer += 1
        for j in range(n):
            if valid(word, words[j]) and not visited[j]:
                stack.append(j)
            if word == target:
                return answer
    return 0