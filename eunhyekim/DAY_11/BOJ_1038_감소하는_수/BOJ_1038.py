N = int(input())
cache = [[[] for _ in range(10) ] for _ in range(10)]
result = []
for i in range(10):
    cache[i][0].append(i)
    result.append(i)

for i in range(1, 10):
    for j in range(10):
        num_lst = []
        for k in range(j):
            num_lst.extend([j*(10**i) + nums for nums in cache[k][i-1]])
        cache[j][i] = num_lst
        result.extend(num_lst)
        if len(result) > N:
            break
    if len(result) > N:
        break
# print(*cache, sep="\n")
# print(result)
# print(len(result))
if N < len(result):
    print(result[N])
else:
    print(-1)
