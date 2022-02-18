N = int(input())
graph = [list(input()) for i in range(N)]
answer = 1


def count():
    global answer
    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if graph[i][j] == graph[i][j+1]:
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt = 1

    for i in range(N):
        cnt = 1
        for j in range(N-1):
            if graph[j][i] == graph[j+1][i]:
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt = 1


for i in range(N):
    for j in range(N-1):
        graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
        count()
        graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]

for i in range(N):
    for j in range(N-1):
        graph[j][i], graph[j+1][i] = graph[j+1][i], graph[j][i]
        count()
        graph[j][i], graph[j+1][i] = graph[j+1][i], graph[j][i]

print(answer)
