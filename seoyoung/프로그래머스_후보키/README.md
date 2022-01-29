## 프로그래머스 후보키

### 풀이 과정

```txt
 ✅ 모든 조합을 찾기 위해서 combination을 사용함 (from itertools import combinations)
 ✅ 조합들을 반복문으로 돌면서 유일성을 확인한 후 유일성을 만족하는 튜플 배열에 한해서 최소성을 확인
 ✅ 기존의 유일성과 최소성을 모두 만족하는 후보키들의 부분집합이면 현재 후보키는 최소성에 의해 후보키가 될 수 없음을 이용해서 최소성을 확인함
    -> 부분집합 여부를 확인하기 위해 issubset이라는 메소드를 사용함
```

### 코드 구현

사용 언어 : **파이썬**

```python
    from itertools import combinations

def solution(relation):
    row,col=len(relation),len(relation[0])
    combi=[]

    # 속성들의 조합
    for i in range(1,col+1):
        combi.extend(combinations(range(col), i))

    result=[]
    for c in combi:
        tmp = [tuple([rel[key] for key in c]) for rel in relation]

        # 유일성 확인
        if len(set(tmp))==row:
            candidate=True;

            #최소성 확인
            for i in result:
                if set(i).issubset(set(c)):
                    candidate=False
                    break

            if candidate: result.append(c)

    return len(result)
```
