## 풀이

오름차순으로 정렬을 해준 뒤 budget을 넘기지 않을 때까지 더해주면서 구해주었습니다.

## 코드
```python
def solution(d, budget):
    answer = 0
    total = 0
    d.sort()
    for i in range(len(d)):
        if total + d[i] <= budget:
            total += d[i]
            answer += 1
        else: return answer
    return answer
```