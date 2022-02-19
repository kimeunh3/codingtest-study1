## 풀이

이분탐색으로 풀어주었습니다.  

걸리는 시간의 최솟값을 구해야할 값으로 두고 이분탐색을 합니다.  

lo와 hi를 각각 가능한 최솟값과 최댓값으로 초기화해줍니다.  
 - lo = 사람 수(n)와 심사관의 수(len(times))가 같고 모든 심사관이 걸리는 시간이 1분으로만 이루어져 있을 때
 - hi = 가장 오래걸리는 심사관(max(times))이 모든 사람(n)을 심사할 때

mid시간 내에 각각 심사관들이 심사할 수 있는 사람들의 수를 done에 더해줍니다.  
done의 수가 n을 넘기거나 같아진다면 심사할 수 있는 충분한 시간이 되기 때문에 바로 break해줍니다.  

done의 수가 더 많다면 hi의 값을 줄여 더 적은 시간범위에서,  
done의 수가 모자라다면 lo의 값을 늘려 더 많은 시간범위에서 찾을 수 있게 합니다.  

done의 수가 많을 때는 최소는 아니더라도 조건에 충족한 값이니 answer를 update해줍니다.  

## 코드
```python
def solution(n, times):
    answer = 0
    lo, hi = 1, max(times)*n
    while lo <= hi:
        mid = (lo + hi) // 2
        done = 0
        for time in times:
            done += mid // time
            if done >= n:
                break
        if done >= n:
            hi = mid - 1
            answer = mid
        else:
            lo = mid + 1
    return answer
```