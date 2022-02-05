## 프로그래머스 두 개 뽑아서 더하기

### 풀이 과정

```txt
✅ 이중 for문으로 배열의 원소들의 합이 answer 배열에 포함되어 있지 않으면 추가
✅ 풀고나서 보니 set 사용해도 되겠다 싶었다.
```

### 코드 구현

사용 언어 : **파이썬**

```python
def solution(numbers):
    answer = []

    for i in range(0,len(numbers)):
        for j in range(i+1,len(numbers)):
            if (numbers[i]+numbers[j]) not in answer:
                answer.append(numbers[i]+numbers[j])

    return sorted(answer)
```
