# import sys
#
# N = int(sys.stdin.readline())  # 컴퓨터의 개수
# connect = int(sys.stdin.readline())  # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
#
# connect_list = set()
# virus = [1]
#
# for i in range(connect):
#     connect_list.add(tuple(map(int, sys.stdin.readline().split())))
#
# check = 0
#
# while check != -1:
#     for i in connect_list:
#         if i[0] in virus:
#             if i[1] not in virus:
#                 virus.append(i[1])
#                 connect_list.discard(i)
#             break
#         elif i[1] in virus:
#             if i[0] not in virus:
#                 virus.append(i[0])
#                 connect_list.discard(i)
#             break
#     else:
#         check = -1
#
# print(len(virus)-1)

import sys

computer = int(sys.stdin.readline().rstrip())
connect = int(sys.stdin.readline().rstrip())
visited = [0] * (computer + 1)
total = 0
graph = {}

for i in range(connect):
    key, value = map(int, sys.stdin.readline().rstrip().rsplit())
    
    # 양방향으로 그래프 만들어주기
    if key not in graph:
        graph[key] = [value]
    else:
        graph[key].append(value)

    if value not in graph:
        graph[value] = [key]
    else:
        graph[value].append(key)


def dfs(index):
    # 방문한 적 없으면
    if visited[index] == 0:
        visited[index] = 1
        
        while graph[index]:
            dfs(graph[index].pop(0))


dfs(1)

for num in visited:
    if num == 1:
        total += 1

print(total - 1)
