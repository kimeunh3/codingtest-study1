## 프로그래머스 위장

### 풀이 과정

```txt
✅ 의상 종류별 의상 개수를 저장하는 딕셔너리 clothTypes
✅ headgear가 2개, eyewear가 2개, face가 3개 있다고 생각하면 각 의상이 포함되지 않을 확률까지 포함해서 총 3 * 3 * 4 의 경우의 수가 나올 수 있지만 스파이는 하루에 최소 1개의 의상은 입으므로 아무것도 착용하지 않는 경우의 수 1개를 제외한 3*3*4-1=35가지의 조합을 입을 수 있습니다.
```

### 코드 구현

사용 언어 : **파이썬**

```python
def solution(clothes):
    answer = 1
    clothTypes = {}

    for cloth in clothes:
        if cloth[1] not in clothTypes:
            clothTypes[cloth[1]] = 0
        clothTypes[cloth[1]] += 1

    for t in clothTypes:
        answer *= (clothTypes[t]+1)

    return answer-1

```
