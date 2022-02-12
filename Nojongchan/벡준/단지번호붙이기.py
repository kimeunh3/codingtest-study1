import sys
from collections import deque

N = int(sys.stdin.readline()) 
map = [ list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N) ]

dy = [0,1,0,-1]
dx = [1,0,-1,0]

count_list = []

def bfs(x, y):
  Q = deque()
  Q.append()
  count = 0
  while Q:
      y, x = Q.popleft()
      count += 1
      for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]
        if 0 <= nx < N and 0 <= ny and map[ny][nx]:
          Q.append(nx, ny)


