''' 프로그래머스 단어변환 

- "가장 짧은" ==> BFS
- 차례대로 que에 넣고 단어를 순차적으로 돌면서 아직 
  방문하지 않고, 단어간 차이가 1개일 경우에 그 단어를 que에 넣음
- 꺼낸 단어가 target과 같아질 때까지 반복.
'''


from collections import deque

def diff_num(w1, w2):
    diff_cnt = 0
    for i, j in zip(w1, w2):
        if i != j:
            diff_cnt += 1
    
    return diff_cnt
    
def solution(begin, target, words):
    if target not in words: return 0
    
    cnt = 0
    dq = deque()
    dq.append((begin, cnt))
    visited = [0] * len(words)
    
    while dq:
        word_now, cnt = dq.popleft()
        
        if word_now == target:
            return cnt
        for i, word in enumerate(words):
            if diff_num(word_now, word) == 1 and not visited[i]:
                cnt += 1
                visited[i] = 1
                dq.append([word, cnt])