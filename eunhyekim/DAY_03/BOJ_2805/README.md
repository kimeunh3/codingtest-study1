## 풀이  

이분탐색을 이용하여 풀었습니다.  

우선 나무들의 높이를 저장해둔 trees를 내림차순으로 정렬해줍니다.  

이분탐색으로 찾을 값을 설정할 수 있는 높이의 최댓값(height)으로 두기 위해 lo와 hi를 height이 가질 수 있는 최솟값, 최댓값으로 초기화해줍니다.  
 - lo = 0 (모든 나무를 다 쓰는 경우)
 - hi = 가장 높은 나무보다 1 작은 값 (N이 1인경우)

mid를 lo와 hi의 중간 값으로 설정한 뒤, mid로 height를 설정했을 때 얻을 수 있는 나무의 길이의 합을 cnt로 구해줍니다.  
trees에 있는 나무들을 찾아주며 trees는 내림차순이므로 tree가 mid보다 작은 순간 나머지 나무들도 mid보다 작으므로 더이상 더해줄 필요가 없기때문에 break를 해줍니다.  
또한 cnt가 가져가려고 하는 나무의 길이(M)을 이미 넘어섰다면 조건을 만족했기 때문에 break를 해줍니다.  

cnt가 M보다 크거나 같을 때는 lo의 범위를 줄여 다음 mid의 값을 더 크게 만들어줍니다. (mid값이 커지면 cnt의 값이 작아짐)  
또한 구하고 있는 답일 수도 있으니 현재 height값과 mid를 비교해 더 큰값으로 height를 update해줍니다.  

cnt가 M보다 작을 때는 hi의 범위를 줄여 다음 mid의 값을 더 작게 만들어줍니다. (mid값이 작아지면 cnt의 값이 커짐)  

## 코드  
```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)
lo, hi = 0, trees[0]-1
height = 0
while lo <= hi:
    mid = (lo + hi) // 2
    cut = 0
    for tree in trees:
        if tree < mid:
            break
        if cut >= M:
            break
        cut += tree - mid
    if cut >= M:
        lo = mid + 1
        height = max(height, mid)
    else:
        hi = mid - 1
print(height)
```
