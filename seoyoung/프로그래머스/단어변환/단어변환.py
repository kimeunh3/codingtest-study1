from collections import deque


def countLetters(cur, word):
    cnt = 0
    for i in range(len(cur)):
        if cur[i] != word[i]:
            cnt += 1

    if cnt == 1:
        return True
    return False


def solution(begin, target, words):
    if target not in words:
        return 0

    visited = [-1]*(len(words))
    queue = deque()
    queue.append(begin)
    flag = False

    while queue:
        cur = queue.popleft()

        for i in range(len(words)):
            if countLetters(cur, words[i]) and visited[i] == -1:
                queue.append(words[i])
                if cur == begin:
                    visited[i] = 1
                else:
                    visited[i] = visited[words.index(cur)]+1

                if words[i] == target:
                    flag = True
                    break
        if flag:
            break

    return visited[words.index(target)]
