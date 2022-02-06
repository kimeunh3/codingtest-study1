# import sys
# input = sys.stdin.readline

house = 0


def dfs(x, y):
    global house

    if x <= -1 or x >= N or y <= -1 or y >= N or graph[x][y] == 0:
        return False

    house += 1
    graph[x][y] = 0
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True


N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))
houses = []

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            houses.append(house)
            house = 0

houses.sort()

print(len(houses))
for i in range(len(houses)):
    print(houses[i])
