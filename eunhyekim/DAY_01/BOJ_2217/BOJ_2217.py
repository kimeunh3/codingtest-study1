N = int(input())
ropes = [ int(input()) for _ in range(N) ]
ropes.sort()
cache = [0 for _ in range(N)]
for i in range(N):
    cache[i] = ropes[i]*(len(ropes)-i)
print(max(cache))