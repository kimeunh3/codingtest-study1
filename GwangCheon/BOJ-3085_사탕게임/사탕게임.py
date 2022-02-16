n = int(input())
candies = []
answer = 1

for i in range(n):
    temp = []
    temp_str = input()
    for j in range(n):
        temp.append(temp_str[j])
    candies.append(temp)


# 몇개 먹을 수 있는지 찾는 함수
def search():
    global answer
    for i in range(n):
        count = 1
        for j in range(n - 1):
            if candies[i][j] == candies[i][j + 1]:
                count += 1
                answer = max(count, answer)
            else:
                count = 1
    for i in range(n):
        count = 1
        for j in range(n - 1):
            if candies[j][i] == candies[j + 1][i]:
                count += 1
                answer = max(count, answer)
            else:
                count = 1


# [모든 인접한 두 자리 뒤집어보고 찾기]
# 가로 뒤집기
for i in range(n):
    for j in range(n - 1):
        candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]
        search()
        candies[i][j], candies[i][j + 1] = candies[i][j + 1], candies[i][j]

# 세로 뒤집기
for i in range(n):
    for j in range(n - 1):
        candies[j][i], candies[j + 1][i] = candies[j + 1][i], candies[j][i]
        search()
        candies[j][i], candies[j + 1][i] = candies[j + 1][i], candies[j][i]

print(answer)
