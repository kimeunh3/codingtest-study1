## 풀이

두 개의 숫자를 더해 추가해주었습니다. 중복은 set을 사용해 처리해주었고, 마지막에는 정렬된 list로 return 해주었습니다.

## 코드
```python
def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.add(numbers[i]+numbers[j])
    return sorted(answer)
```