## 프로그래머스 입국심사

### 알고리즘

- 이분탐색

### 풀이 과정

```txt
✅ times 배열 안의 time의 값이 최대 1,000,000,000분일 수 있다는 점에서 단순히 for문을 돌려서 찾으면 안되겠다는 판단 -> 이분탐색 사용해서 검색 범위를 줄여보자고 생각함
✅ times 배열 안의 원소를 time이라고 하면 심사시간//time 을 합친 것이 n보다 클 때 심사 시간 안에 모든 사람이 심사 받을 수 있으므로 답으로 심사시간을 저장함
➡️ 처음에 심사시간//time 을 합친 것이 n과 같으면 즉시 답을 리턴하는 코드로 구현했었는데, 그 심사시간이 최소값이라는 보장이 없으므로 계속해서 이분탐색을 하며 구해줘야 한다
✅ times 배열 안의 원소를 time이라고 하면 심사시간//time 을 합친 것이 n보다 작다면 심사시간 안에 모든 사람이 심사를 받을 수 없기 때문에 start=mid+1해서 심사시간을 현재 범위보다 큰 범위에서 탐색할 수 있도록 함
```

### 코드 구현

사용 언어 : **파이썬**

```python
def solution(n, times):
    answer = 0
    start, end = 1, max(times)*n

    while start <= end:
        mid = (start+end)//2

        people = 0
        for time in times:
            people += mid//time

        if people >= n:
            answer = mid
            end = mid-1
        else:
            start = mid+1

    return answer
```
