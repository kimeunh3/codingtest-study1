# 회의의 수 입력
import sys

N = int(input())

# 회의 시간 입력(정렬 전)
schedule = []
for i in range(N):
    start, last = map(int, sys.stdin.readline().split())
    schedule.append([start, last])


schedule.sort(key=lambda x: (x[1], x[0]))
#회의 종료시간 기준 정렬

count = 1
last = schedule[0][1]
for k in range(1, N):
    if last <= schedule[k][0]:
        last = schedule[k][1]
        count += 1
print(count)