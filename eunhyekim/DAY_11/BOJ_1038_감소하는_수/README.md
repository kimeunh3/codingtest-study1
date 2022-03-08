## 풀이  

동적계획법으로 풀었습니다.  

cache는 다음과 같습니다:
```python
# cache[i][j] = 숫자 i로 시작하는 j+1 자릿수의 감소하는 숫자들의 배열
# i = 0
cache[0][0] = [0] # j = 0
# i = 1
cache[1][0] = [1] # j = 0
cache[1][1] = [10] # j = 1
# i = 2
cache[2][0] = [2] # j = 0
cache[2][1] = [20, 21] # j = 1
cache[2][2] = [210] # j = 2
```
  
다음 자릿수의 배열은 시작하는 숫자보다 작은 숫자로 시작하는 한 자릿수 적은 감소하는 수를 시작하는 숫자 뒤에 붙여주면 됩니다.
```python
for s in range(start_num):
    num_lst.extend([start_num*(10**nth) + nums for nums in cache[s][nth-1]])
```
그렇게 해서 만들어진 num_lst를 result에 extend 해줍니다.  
만약 result의 길이가 N보다 길 경우, 원하는 답을 찾았기 때문에 바로 break해줍니다.  

혹시 다 찾아주어도 result의 길이가 N보다 짧을 때에는 N번째의 감소하는 수는 존재하지 않으므로  
-1을 출력해주고, 그렇지 않을 때는 result\[N\]을 출력해줍니다.  

## 코드  
```python
N = int(input())
cache = [[[] for _ in range(10) ] for _ in range(10)]
result = []

for i in range(10):
    cache[i][0].append(i)
    result.append(i)

for nth in range(1, 10):
    for start_num in range(10):
        num_lst = []
        for s in range(start_num):
            num_lst.extend([start_num*(10**nth) + nums for nums in cache[s][nth-1]])
        cache[start_num][nth] = num_lst
        result.extend(num_lst)
        if len(result) > N:
            break
    if len(result) > N:
        break

if N < len(result):
    print(result[N])
else:
    print(-1)
```