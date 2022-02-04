## 풀이

동적계획법을 활용한 완전탐색으로 풀었습니다.  

cache는 다음과 같습니다.  
```
cache[num] = [] num개의 N으로 만들 수 있는 수
```

각각의 cache에는 5, 55, 555, 5555 ... 와 같은 수를 넣어줍니다.  
cache\[1\]에는 N만 들어갈 수 있고, cache\[2\]는 N를 이용하여 사칙연산을 한 값들이 들어가게됩니다. 예를 들면 5+5, 5-5, 5*5, 5/5가 됩니다.  
cache\[3\]부터는 cache\[1\]과 cache\[2\]사이의 사칙연산을 한 값들이 들어가게됩니다.  
이런식으로 만들어 낼 수 있는 모든 수를 찾아주기 위해 cache\[8\]까지 계산을 해주되, +, *는 순서가 바뀌어도 값이 같지만 -와 /는 순서가 바뀌면 값이 달라지기 때문에 반대 순서도 고려를 해주어야합니다. +, *로 인한 중복은 set으로 처리해줍니다.  

각각의 cache\[num\]에서 number가 있는지 찾아보고 있다면 바로 answer에 num을 저장하고 break를 해준 뒤 answer를 return해줍니다. 만약 찾지 못하고 break를 해주지 못했을 때는 -1을 return 합니다. 

## 코드
```python
def solution(N, number):
    answer = 0
    cache = [ set() for _ in range(9) ]
    # cache[num] = [] num개의 N으로 만들 수 있는 수
    # N이 5라면
    for i in range(1, 9):
        cache[i].add(int(str(N)*i)) # 5, 55, 555, 5555, 55555 ...
    for num in range(1, 9):
        for j in range(1, num):
            # +, *는 순서가 바뀌어도 값이 같지만 -와 /는 순서가 바뀌면 값이 달라지기 때문에 반대 순서도 고려를 해주고
            # +, *로 인한 중복은 set으로 처리
            for a in cache[j]:
                for b in cache[num-j]:
                    cache[num].add(a + b)
                    cache[num].add(a - b)
                    cache[num].add(a * b)
                    if b != 0: # division by 0를 예방하기 위함
                        cache[num].add(a // b)
        if number in cache[num]:
            answer = num
            break
    else:
        return -1
    
    return answer
```