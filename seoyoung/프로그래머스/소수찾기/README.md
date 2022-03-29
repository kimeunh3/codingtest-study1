## 프로그래머스 소수찾기

### 풀이과정

```
- 소수인지 판별하기 위한 is_prime_number 함수
- 2차원 배열인 num_arr을 1차원 배열로 평평하게 만들어주기 위해서 sum(num_arr,[])
- num_arr에 저장되는 값들은 문자열
    => set로 중복을 제거해주더라도 "001"과 "1"와 같은 값이 다른 값으로 인식하고 있음
    => 그냥 num_arr의 숫자가 소수이면 answer+=1 해주는 것으로 해결이 안됨
    => answer 배열에 소수로 판명난 숫자를 넣어주고 값이 이미 있으면 안 넣는 식으로 해결
```

### 코드 구현

사용 언어 : **파이썬**

```python
import itertools

def is_prime_number(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    num_arr = []

    # 문자열 numbers로 만들 수 있는 숫자를 permutation을 이용해서 만들고 num_arr에 저장
    # num_arr=[[길이 1 숫자 배열],[길이가 2인 숫자 배열],,,,[길이가 numbers인 숫자 배열]] 형태로 저장됨
    for i in range(1, len(numbers)+1):
        num_arr.append(list(map(''.join, itertools.permutations(numbers, i))))

    # 2차원 배열을 1차원으로 평평하게 펴주고 중복 제거하기 위해 set 사용
    num_arr = set(sum(num_arr, []))

    # num이 소수이고 answer 배열에 없으면 int(num)을 answer배열에 넣어주기
    for num in num_arr:
        if is_prime_number(int(num)) and int(num) not in answer:
            answer.append(int(num))

    return len(answer)
```
