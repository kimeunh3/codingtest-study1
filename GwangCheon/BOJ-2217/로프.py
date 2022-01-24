import sys

n = int(input())

rope = [int(sys.stdin.readline()) for i in range(n)]

rope.sort(reverse=True)

weight = [rope[i] * (i + 1) for i in range(n)]
print(max(weight))
