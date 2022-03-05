from itertools import combinations

N = int(input())
decreasing = []

for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        comb = list(comb)
        comb.sort(reverse=True)
        decreasing.append(int("".join(map(str, comb))))
decreasing.sort()

if N >= len(decreasing):
    print(-1)
else:
    print(decreasing[N])
