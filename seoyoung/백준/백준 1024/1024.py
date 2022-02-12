N, L = map(int, input().split())
start = -1
len = L

for i in range(L, 101):
    s = N/i - (i-1)/2
    if s == int(s) and s >= 0:
        start = s
        len = i
        break

if start == -1:
    print(-1)
else:
    for i in range(len):
        print(int(start)+i, end=' ')
