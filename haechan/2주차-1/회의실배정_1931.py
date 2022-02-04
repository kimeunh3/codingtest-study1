'''백준 회의실 배정 1931번

- 회의시간이 빨리끝나는 순으로 정렬
- 회의 시작시간이 직전 회의종료시간보다 크거나 같으면 해당 미팅을 진행할 수 있다는 뜻 => meet_cnt += 1
'''

n = int(input())
meeting_list = []
for _ in range(n):
    st, end = map(int, input().split())
    meeting_list.append((st, end))

meeting_list.sort(key=lambda x: (x[1], x[0]))

meet_cnt = 0
before_end= 0
for meeting in meeting_list:
    st, end = meeting[0], meeting[1]

    if st >= before_end:
        meet_cnt += 1
        before_end = end

print(meet_cnt)