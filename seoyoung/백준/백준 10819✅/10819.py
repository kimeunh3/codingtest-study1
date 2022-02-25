from itertools import permutations
N = int(input())
arr = list(map(int, input().split()))
arr_permu = list(permutations(arr, N))
answer = 0

for arr in arr_permu:
    diff = 0
    for i in range(1, N):
        diff += abs(arr[i]-arr[i-1])
    answer = max(answer, diff)

print(answer)
