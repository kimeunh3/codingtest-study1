'''백준 정수삼각형 1932번

- 각 로우마다 합의 값을 갱신해가며 최하단 로우까지 진행한 뒤, max값을 출력
- 가장자리의 경우 index 0번째와 -1번째를 각각 직전 row의 0번째와 -1번째를 합함
- 중간 index는 직전 row의 index와 index-1의 값 중 큰 값을 합하도록 함
'''

n = int(input())
rows = []
for _ in range(n):
    rows.append(list(map(int, input().split())))

top = rows[0][0]
after = rows.copy()
for i in range(1, n):
    for idx,val in enumerate(after[i]):
        if idx == 0:
            after[i][idx] += after[i-1][0]
        elif idx == len(after[i]) - 1:
            after[i][idx] += after[i-1][-1]
        else:
            after[i][idx] += max([after[i-1][idx], after[i-1][idx-1]])
    
print(max(after[-1]))