## 프로그래머스 조이스틱

### 풀이 과정

```txt
✅ 그리디로 풀었더니 왼쪽으로 갔다가 오른쪽으로 이동하는 테스트 케이스를 해결하지 못함
✅ 완전탐색으로 해결
➡️ 오른쪽으로 이동, 왼쪽으로 이동, 오른쪽으로 이동하다가 왼쪽으로 이동, 왼쪽으로 이동하다가 오른쪽으로 이동하는 경우를 모두 나눠서 answer값을 구해준 다음, 4가지 경우 중 최소값을 최종적으로 리턴하도록 함
```

### 코드 구현

사용 언어 : **파이썬**

```python
import sys


def solution(name):
    moves = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in name]
    pos = 0

    # 왼쪽으로 쭉 이동 + 오른쪽으로 갔다가 왼쪽으로 이동
    ans1 = sys.maxsize

    for i in range(0, len(moves)):
        pos = 0
        moves1 = moves[:]
        ans_temp = 0
        direction = False
        while True:
            ans_temp += moves1[pos]
            moves1[pos] = 0
            if sum(moves1) == 0:
                break

            if pos == i or pos == i-len(moves):
                direction = True

            # 방향 전환
            if direction:
                pos -= 1
            else:
                pos += 1
            ans_temp += 1
        if ans_temp < ans1:
            ans1 = ans_temp

    # 오른쪽으로 쭉 이동 + 왼쪽으로 갔다가 오른쪽으로 이동
    ans2 = sys.maxsize

    for i in range(len(moves)):
        pos = 0
        moves2 = moves[:]
        ans_temp = 0
        direction = False

        while True:
            ans_temp += moves2[pos]
            moves2[pos] = 0

            if sum(moves2) == 0:
                break

            if pos == i or pos == i-len(moves):
                direction = True

            # 방향 전환
            if direction:
                pos += 1
            else:
                pos -= 1

            ans_temp += 1

        if ans_temp < ans2:
            ans2 = ans_temp

    return min(ans1, ans2)
```
