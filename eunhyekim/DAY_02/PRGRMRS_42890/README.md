## 풀이

itertool의 combinations를 응용해 풀어보았습니다. combination과 permutation의 작동방식은 아래와 같습니다.  
```python
from itertools import permutations, combinations
items = [1, 2, 3, 4, 5]
# [(1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
print(list(combinations(items, 2)))
# [(1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 3), (2, 4), (2, 5), (3, 1), (3, 2), (3, 4), (3, 5), (4, 1), (4, 2), (4, 3), (4, 5), (5, 1), (5, 2), (5, 3), (5, 4)]
print(list(permutations(items, 2)))

```
모든 경우의 수를 확인해주기 위해 1개부터 속성의 갯수만큼 combination을 구해주어 확인해보았습니다.  

최소성을 체크하기 위해 현재의 조합중 answer에 들어가있는 조합을 subset으로 가지는 조합이 있다면 제외해주었습니다.  

combi에 있는 조합들로 이루어진 학생들의 정보를 하나의 string으로 만들어 비교해주었고, 구별가능하다면 answer에 넣어주었습니다.  

반복해주면서 마지막에는 answer의 길이로 return해주었습니다.  

## 코드
```python
from itertools import combinations

def check_minimality(answer, combi):
    new_combi = combi.copy()
    # 이미 answer에 들어있는 답이 combi의 subset일 경우
    # combi에서 제외해준다 (최소성 체크)
    for ans in answer:
        for c in combi:
            if ans.issubset(c):
                if c in new_combi:
                    new_combi.remove(c)
    # 제외해야할 set이 있었을 경우 combi를 new_combi로 바꿔준다.
    return new_combi

def solution(relation):
    answer = []
    num_stu = len(relation)
    num_col = len(relation[0])
    for i in range(1, num_col+1):
        # i개 만큼의 col을 가지는 combination의 리스트
        combi = [set(c) for c in combinations(range(num_col), i)]
        # 최소성 체크
        combi = check_minimality(answer, combi)
        # 유일성 체크
        for col in combi:
            combi_set = set()
            # 각각 학생들의 정보를 하나의 string으로 만들어 set에 넣어준다
            for stu in relation:
                combi_set.add(''.join([stu[c] for c in col]))
            # 중복되었다면 set의 길이는 num_stu보다 작을것이고
            # 그렇지 않다면 길이는 같다. 같다는건 모든 학생을 구별 가능하다는 것
            if len(combi_set) == num_stu:
                answer.append(col)
    
    return len(answer)
```