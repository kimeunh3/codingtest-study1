## 풀이

DFS로 풀어주었습니다.  

시작하는 수가 양수일 때와 음수일 때를 넣어준 뒤,  
해당 수에서 다음 index의 수를 더해준 값과, 빼준 값을 queue에 넣어줍니다.  

모든 수를 다 썼을 때, target과 num이 같다면 answer를 증가시켜줍니다.  

## 코드
```python
def solution(numbers, target):
    answer = 0
    queue = [[numbers[0], 0], [-1*numbers[0], 0]]
    while(queue):
        num, idx = queue.pop()
        idx += 1
        if idx < len(numbers):
            queue.append([num+numbers[idx], idx])
            queue.append([num-numbers[idx], idx])
        else:
            if num == target:
                answer += 1
    return answer
```