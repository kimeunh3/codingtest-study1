import sys
from collections import deque

iuput = sys.stdin.readline

N = int(input())
timeline = []
for _ in range(N):
    timeline.append(tuple(map(int, input().split())))
timeline = deque(sorted(timeline, key=lambda x: (x[1], x[0])))
prev_end = 0
meetings = 0
while timeline:
    start, end = timeline.popleft()
    if prev_end <= start:
        meetings += 1
        prev_end = end
print(meetings)