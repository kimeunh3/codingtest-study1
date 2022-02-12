## 프로그래머스 예산

### 풀이 과정

```txt
✅ 처음에는 모든 조합을 combination으로 구해서 검사하는 식으로 했는데 시간 초과
✅ 최대 몇 개의 부서에 물품을 지원할 수 있는지 구하기 위해서는 신청금액이 작은 원소부터 budget에서 빼야 함
✅ 원소를 빼다가 budget이 0보다 작아졌을 때 그 때까지의 원소의 개수를 리턴하면 됨
```

### 코드 구현

사용 언어 : **파이썬**

```python
def solution(d, budget):
    answer = 0

    for i in sorted(d):
        budget-=i
        if budget<0:
            break
        answer+=1

    return answer
```
