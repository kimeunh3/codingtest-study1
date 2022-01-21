## 풀이  

문제의 k개의 로프를 사용하여 중량이 w인 물체를 들어올릴때 각각의 로프에는 고르게 w/k만큼의 중량이 걸리게 된다고 한말을 다시 이해하면 최대로 올릴 수 있는 <strong>중량은 로프 중 가장 적은 중량의 로프 * 연결하는 로프의 수</strong>가 됩니다.  

그래서 로프가 버틸 수 있는 중량을 배열로 받아준 뒤, 배열을 오름차순으로 정렬해줍니다. cache\[i\]에는 ropes\[i\]의 로프부터 나머지 로프를 모두 사용했을때의 최대 중량을 저장해줍니다. 정렬을 해주었기 때문에 나머지 로프들은 최소 ropes\[i\]만큼은 버틸 수 있기 때문에 다 포함해 주는 것이 최대 중량이 되기 때문입니다.  

그래서 cache의 값은 다음과 같이 됩니다.  
```
cache[i] = ropes[i] * (i번째 로프를 포함한 나머지 로프의 개수)
```

for loop을 N만큼 돌려 cache를 update해주고 cache의 max값을 출력해줍니다.


## 코드  
```python
N = int(input())
ropes = [ int(input()) for _ in range(N) ]
ropes.sort()
cache = [0 for _ in range(N)]
for i in range(N):
    cache[i] = ropes[i]*(len(ropes)-i)
print(max(cache))
```