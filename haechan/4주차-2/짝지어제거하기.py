'''프로그래머스 짝지어 제거하기'''

def solution(s):
    stack = []
    
    for i in range(len(s)):
        if not stack: # 스택이 비어있으면
            stack.append(s[i]) # 스택에 직전 알파벳을 담는다
        else:
            if stack[-1] == s[i]: # 직전 알파벳과 현재 알파벳이 같다면
                stack.pop() # 직전 알파벳 삭제
            else:
                stack.append(s[i]) # 같지 않으면 직전 알파벳 갱신
    
    if not stack: return 1
    else: return 0