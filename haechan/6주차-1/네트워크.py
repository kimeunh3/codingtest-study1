'''프로그래머스 네트워크'''

from collections import deque

def solution(n, computers):
    
    networks = 0
    visited = [0] * n
    
    while 0 in visited: # 모든 컴퓨터를 방문해야 bfs를 종료
        dq = deque()
        x = visited.index(0)
        dq.append(x)
        visited[0] = True
        
        while dq: # 첫번째 컴퓨터의 연결정보를 기준으로 방문처리
            node = dq.popleft()

            for i in range(n):
                if not visited[i] and computers[node][i]:
                    dq.append(i)
                    visited[i] = True
        networks += 1

    return networks