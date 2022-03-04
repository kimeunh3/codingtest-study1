## 백준 10819 차이를 최대로

### 코드 구현

사용 언어 : **파이썬**

```python
from itertools import permutations

N = int(input())
arr = list(map(int, input().split()))
# 입력받은 배열의 원소로 만들 수 있는 모든 순열들을 저장한 배열
arr_permu = list(permutations(arr, N))
answer = 0

for arr in arr_permu:
    diff = 0
    # 현재 배열에서 얻을 수 있는 인접한 원소의 차이의 합을 diff에 저장
    for i in range(1, N):
        diff += abs(arr[i]-arr[i-1])
    # diff와 이전 순열들에서 찾은 최댓값을 비교하여 더 큰 값을 answer에 저장
    answer = max(answer, diff)

print(answer)

```
