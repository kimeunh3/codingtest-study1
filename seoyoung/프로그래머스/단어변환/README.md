## 프로그래머스 단어변환

### 코드 구현

사용 언어 : **파이썬**

```python

from collections import deque

# 단어 변환 가능 여부 반환 (가능 true 불가능 false)
def changeWord(cur, word):
    cnt = 0
    for i in range(len(cur)):
        if cur[i] != word[i]:
            cnt += 1

    if cnt == 1:
        return True
    return False

def solution(begin, target, words):
    # words에 target 단어가 포함되지 않은 경우 아래 코드를 실행할 필요없이 종료
    if target not in words:
        return 0

    visited = [-1]*(len(words))
    queue = deque()
    queue.append(begin)
    flag = False

    while queue:
        cur = queue.popleft()

        for i in range(len(words)):
            # word[i]가 cur로 바뀔 수 있고, word[i]를 아직 방문하지 않았다면
            if changeWord(cur, words[i]) and visited[i] == -1:
                queue.append(words[i])
                # word에 cur이 포함되어 있지 않아서 if-else문으로 나눠야 했음
                if cur == begin:
                    visited[i] = 1
                else:
                    visited[i] = visited[words.index(cur)]+1

                # 만약 word[i]가 target이면 for루프 -> while루프 빠져나가서 답 출력하면 됨
                if words[i] == target:
                    flag = True
                    break
        if flag:
            break

    # 만약 배열에 target 단어가 있지만 단어 변환이 안돼서 방문하지 못한 경우 처리
    if visited[words.index(target)]==-1:
        visited[words.index(target)]=0

    return visited[words.index(target)]
```
