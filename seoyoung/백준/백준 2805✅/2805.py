import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)

while start <= end:
    mid = (start+end)//2
    temp = M

    for tree in trees:
        if tree > mid:
            temp -= (tree-mid)

    if temp <= 0:
        start = mid+1
    else:
        end = mid-1

print(end)
