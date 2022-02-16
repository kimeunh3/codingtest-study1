import sys
input = sys.stdin.readline

N = int(input())
schedule = [ list(map(int, input().split())) for _ in range(N) ]
cache = [[0, 0] for _ in range(N)]
# print("------------------------------------------------")
for i in range(N):
    if i + schedule[i][0]-1 >= N:
        continue
    cache[i][1] += schedule[i][1]
    for j in range(i+1, N):
        if j >= i + schedule[i][0]:
            cache[j][0] = max(cache[i][0], cache[i][1], cache[j][0])
            cache[j][1] = max(cache[i][0], cache[i][1], cache[j][1])
#     print(*cache, sep="\n")
#     print("------------------------------------------------")

print(max(map(max, cache)))
