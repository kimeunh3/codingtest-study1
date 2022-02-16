T = int(input())
field = [[0 for i in range(T)] for i in range(T)]
max = 0


def check(arr):
    n = len(arr)
    answer = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > answer:
                answer = cnt
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > answer:
                answer = cnt
    return answer


for i in range(T) :
    tmp = input()
    for j in range(T) :
        field[i][j] = tmp[j]
for i in range(T) :
    for j in range(T) :
            if j < len(field[i]) - 1 :
                field[i][j], field[i][j+1] = field[i][j+1], field[i][j]
                tmp = check(field)
                field[i][j], field[i][j + 1] = field[i][j + 1], field[i][j]
                if tmp > max :
                    max = tmp
            if i < len(field) - 1 :
                field[i][j], field[i+1][j] = field[i+1][j], field[i][j]
                tmp2 = check(field)
                field[i][j], field[i + 1][j] = field[i + 1][j], field[i][j]
                if tmp2 > max :
                    max = tmp2

print(max)








