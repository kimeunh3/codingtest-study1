# 5:08 PM 시작
# 6:02 PM pypy 제출로 성공
# 6:29 PM input 방식 바꿔서 python 제출로 성공

# Counter 모듈을 사용하지 않은 풀이 888ms
from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())
arr = []
cnt = defaultdict(int)
mean = 0
max_num = -4001
min_num = 4001

for _ in range(N):
  num = int(input())
  arr.append(num)
  mean += num
  cnt[num] -= 1
  max_num = max(max_num, num)
  min_num = min(min_num, num)

cnt = sorted(cnt.items(), key=lambda x: (x[1], x[0]))

arr.sort()
mid = N // 2
mean = round(mean/N)
median = arr[mid] if N % 2 else (arr[mid]+arr[mid-1]) // 2
mode = cnt[1][0] if len(cnt) > 1 and cnt[0][1] == cnt[1][1] else cnt[0][0]
range_ = max_num - min_num

print(mean)
print(median)
print(mode)
print(range_)

# Counter 모듈을 사용한 풀이 444ms
from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
arr = [ int(input()) for _ in range(N)]
arr.sort()
length = len(arr)
mid = length // 2
cnt = Counter(arr).most_common(2)
mean = round(sum(arr)/length)
median = arr[mid] if length % 2 else (arr[mid]+arr[mid-1]) // 2
mode = sorted(cnt, key=lambda x: x[0])[1][0] if len(cnt) > 1 and cnt[0][1] == cnt[1][1] else cnt[0][0]
range_ = max(arr) - min(arr)

print(mean)
print(median)
print(mode)
print(range_)