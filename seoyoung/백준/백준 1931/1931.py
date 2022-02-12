import sys
input = sys.stdin.readline

N = int(input())
meetings = []
for i in range(N):
    meetings.append(list(map(int, input().split())))

# 끝나는 시간을 기준으로 오름차순 정렬하며, 끝나는 시간이 같을 경우 시작하는 시간 기준 오름차순 정렬
# 끝나는 시간이 빨라야 다른 회의들을 고려해볼 여지가 있음
# 끝나는 시간이 같을 경우에는 시작 시간이 앞인 것부터 고려해줘야 더 많은 회의를 확보 가능
meetings.sort(key=lambda x: (x[1], x[0]))

last = 0
answer = 0
for start, end in meetings:
    if start >= last:
        answer += 1
        last = end

print(answer)
