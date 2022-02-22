## 풀이

해시 문제라서 dictionary를 이용하여 풀었습니다.  

처음에는 **combination을 쓰는 접근**을 하였으나 후에 dictionary로 구현하는 것이 **더 효율적**임을 깨닫게 되었습니다.  

dictionary를 이용하여 각각 의상 종류에 따라 수를 구해주었습니다.  

그런 뒤에는 경우의 수를 구하는 공식을 사용하였는데,  
이 문제의 경우에는 **모든 의상 종류를 착용하지 않아도 되기 때문에**  
각각 의상 종류의 수에 1을 더한 값(**해당 의상 종류를 입지 않을 경우**)을 answer에 곱해주었습니다.  

그 결과는 **모든 의상 종류를 입지 않을 경우**도 포함하기 때문에 1을 빼준 뒤 return해주었습니다.  

## 코드
```python
from collections import defaultdict

def solution(clothes):
    answer = 1
    kind_dict = defaultdict(int)
    for _, kind in clothes:
        kind_dict[kind] += 1
    keys = list(kind_dict.values())
    for i in range(len(keys)):
        answer *= keys[i]+1

    return answer - 1
```