## 풀이

처음에는 구현 문제인 줄 알고 열심히 풀어보았지만 번번이 효율성 테스트를 통과하지 못했습니다.  

그래서 생각하다 저번에 푼 이전의 값을 고려해주기 위해 **stack을 사용한 괄호문제**가 생각났습니다.  

stack에 각각의 문자를 넣어주기 전, stack에 이미 넣어준 문자가 있다면 마지막에 넣어준 문자와 비교하여  
**같을 때는 stack을 pop**해주고 해당 문자는 넣어주지 않았습니다.  

일치하지 않는다면 **stack에 해당 문자를 추가**해주었고,  
마지막에는 stack에 문자가 남았다면 **문자열을 모두 제거할 수 없었단 뜻**이기 때문에 0을,  
그렇지 않으면 **문자열을 모두 제거**해주었기 때문에 1을 return 해주었습니다.  

## 코드
```python
def solution(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    
    return 0 if stack else 1
```
