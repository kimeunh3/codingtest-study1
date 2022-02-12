## 백준 2805번 나무 자르기

### 알고리즘

- **이분탐색**

### 풀이 과정

```txt
✅ 무작정 for루프 돌리니까 시간 초과 ➡️ 절단기 설정 높이를 구하는 부분의 효율성을 높이기 위해 이분탐색을 사용
✅ 절단기 설정 높이로 잘랐을 때 잘라진 나무 길이의 합이 M보다 크면 절단기 설정 높이가 커도 되므로 start를 현재 절단기 높이+1로 설정
✅ 잘려진 나무 길이의 합이 M보다 작을 때는 절단기 설정 높이를 작게 해서 나무를 더 많이 잘라야 하므로 end를 현재 절단기 높이-1로 설정
✅start=end될 때 while문이 종료되고 그 값이 절단기 높이 최대값
```

### 코드 구현

사용 언어 : **파이썬**

```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)

while start <= end:
    mid = (start+end)//2
    temp = M

    for tree in trees:
        if tree > mid:
            temp -= (tree-mid)

    if temp <= 0:
        start = mid+1
    else:
        end = mid-1

print(end)
```
