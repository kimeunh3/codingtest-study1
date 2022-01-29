# 알고리즘 문제풀이

## 풀이 목록

| # | 날짜 | 문제이름 | 링크 | 풀이 | 완료 | Best |
| :-: | :------: | :--------------------------: | :--------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------: | :--: | :----: |
| 1 | 22-01-25 | 로프 |  [문제](https://www.acmicpc.net/problem/2217)  |  [BOJ-2217](https://kdt-gitlab.elice.io/eunhyekim1223/codingtest-study/-/tree/master/GwangCheon/BOJ-2217)  | ✔ | 신광천 |
| 2 | 22-01-25 | 전쟁-땅따먹기 |  [문제](https://www.acmicpc.net/problem/1270)  |  [BOJ_1270](https://kdt-gitlab.elice.io/eunhyekim1223/codingtest-study/-/tree/master/eunhyekim/DAY_01/BOJ_1270)  | ✔ | 김은혜 |
| 3 | 22-01-25 | 폴짝폴짝 |  [문제](https://www.acmicpc.net/problem/1326)  |  [퐁당퐁당.py](https://kdt-gitlab.elice.io/eunhyekim1223/codingtest-study/-/blob/master/Hosan_Lee/Python_%ED%90%81%EB%8B%B9%ED%90%81%EB%8B%B9.py)  | ✔ | 이호산 |
| 4 | 22-01-25 | 수열의 합 |  [문제](https://www.acmicpc.net/problem/1024)  | [BOJ-1024](https://kdt-gitlab.elice.io/eunhyekim1223/codingtest-study/-/tree/master/GwangCheon/BOJ-1024) | ✔ | 신광천 |
| 5 | 22-01-25 | Fly me to the Alpha Centauri |  [문제](https://www.acmicpc.net/problem/1011)  | [1011. 골드1 Fly to Alphacentaury.py](https://kdt-gitlab.elice.io/eunhyekim1223/codingtest-study/-/blob/master/Nojongchan/1011.%20%EA%B3%A8%EB%93%9C1%20Fly%20to%20Alphacentaury.py) | ✔ |  노종찬 |
| 6 | 22-01-29 | 최소직사각형 |  [문제](https://programmers.co.kr/learn/courses/30/lessons/86491)  | [최소직사각형.py](https://kdt-gitlab.elice.io/eunhyekim1223/codingtest-study/-/blob/master/haechan/1%EC%A3%BC%EC%B0%A8-2/%EC%B5%9C%EC%86%8C%EC%A7%81%EC%82%AC%EA%B0%81%ED%98%95.py) | ✔ | 양해찬 |
| 7 | 22-01-29 | 카펫 |  [문제](https://programmers.co.kr/learn/courses/30/lessons/42842)  | [프로그래머스_카펫](https://kdt-gitlab.elice.io/eunhyekim1223/codingtest-study/-/tree/master/seoyoung/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4_%EC%B9%B4%ED%8E%AB) | ✔ | 배서영 |
| 8 | 22-01-29 | 후보키 |  [문제](https://programmers.co.kr/learn/courses/30/lessons/42890)  | [프로그래머스_후보키](https://kdt-gitlab.elice.io/eunhyekim1223/codingtest-study/-/tree/master/seoyoung/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4_%ED%9B%84%EB%B3%B4%ED%82%A4) | ✔ | 배서영 |
| 9 | 22-01-29 | 단어 변환 |  [문제](https://programmers.co.kr/learn/courses/30/lessons/43163)  | [단어변환.py](https://kdt-gitlab.elice.io/eunhyekim1223/codingtest-study/-/blob/master/Hosan_Lee/%EB%8B%A8%EC%96%B4%EB%B3%80%ED%99%98.py) | ✔ | 이호산 |
| 10 | 22-02-02 | 나무자르기 |  [문제](https://www.acmicpc.net/problem/2805)  | []() | ❌ |  |
| 11 | 22-02-02 | 회의실배정 |  [문제](https://www.acmicpc.net/problem/1931)  | []() | ❌ |  |
| 12 | 22-02-02 | 정수삼각형 |  [문제](https://www.acmicpc.net/problem/1932)  | []() | ❌ |  |
| 13 | 22-02-02 | 단지번호붙이기 |  [문제](https://www.acmicpc.net/problem/2667)  | []() | ❌ |  |

## Tips

- **permutations & combinations**
  ```python
  from itertools import permutations, combinations
  items = [1, 2, 3, 4, 5]
  # [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
  print(list(combinations(items, 2)))
  # [(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)]
  print(list(permutations(items, 2)))
  ```

- **defaultdict**
  ```python
  from collections import defaultdict
  d_dict = defaultdict()
  d_dict[i] += 1 #초기화 없이 사용가능
  ```

- **Counter**
  ```python
  from collections import Counter
  items = [2, 2, 1, 1, 1, 1, 1, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5] # Counter({5: 6, 1: 5, 3: 3, 2: 2, 4: 2})
  str1 = "eeeeelllllllllliiiiiccccccccee" # Counter({'l': 10, 'c': 8, 'e': 7, 'i': 5})
  cnt1 = Counter(items)
  cnt2 = Counter(str1)
  # 가장 많은 top 3
  cnt1.most_common(3) # [(5, 6), (1, 5), (3, 3)]
  cnt2.most_common(3) # [('l', 10), ('c', 8), ('e', 7)]
  ```

- **for-else, while-else 구문**
  ```python
  for or while:
     # 블라블라
     break
  else:
  # break를 통해 루프가 끝나지 않았을 경우에 쓰는 코드
  ```

- **import sys**
  - `sys.setrecursionlimit(limit_number)`
    - 재귀함수 제한 해제하고 싶을 때 ( default = 1000 )
  - `sys.stdin.readline()`
    - 입력 받을 때 ( input 보다 속도상에서 우위, 문자열로 입력받을 때 \n 개행까지 입력받으므로 주의 )  


- **BFS: 큐를 이용 (from collections import deque)**
  - 최단거리 문제 (DFS보다 빠를때가 많음)
- **DFS: 스택를 이용 (python list 사용)**
  - 백트래킹 문제 (모든 경우의 수를 봐야할 때)
