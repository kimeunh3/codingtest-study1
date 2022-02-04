## 풀이

가지치기로 일단 target이 단어에 없다면 변환할 수 없기 때문에 제외해주었습니다.  

DFS로 풀었습니다. 이미 확인해준 단어를 중복하여 확인하지 않기 위해 visited를 만들어주었고, 시작하는 단어랑 한 개의 알파벳만 다른 단어들을 valid함수를 이용해 구별하여 stack에 넣어주었습니다.  

변환할 수 있는지, 방문한적이 없는지를 판단하고 stack에 넣어준 뒤 word가 target이랑 같을 때 단계 수를 세어주던 answer를 return해주었습니다. solution을 찾지 못하고 while loop를 빠져나왔을 때는 0을 return해주었습니다.
## 코드
```python
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
```