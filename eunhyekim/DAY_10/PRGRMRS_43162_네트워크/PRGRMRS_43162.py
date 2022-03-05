def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]
    queue = []
    for i, v in enumerate(visited):
        # 방문하지 않은 노드 찾아서 queue에 넣어주기
        if not v:
            queue.append(i)    
            visited[i] = 1
            # 찾은 노드에서 시작해서 연결된 다른 노드 방문
            while queue:
                com = queue.pop()
                # 연결된 노드 찾아주기
                for j, com2 in enumerate(computers[com]):
                    if not visited[j] and j != com:
                        # 연결된 노드에서 또 다른 연결된 노드 찾아주기 위해 queue에 추가
                        # 연결된 노드를 찾았을 때 바로 방문처리
                        if com2:
                            queue.append(j)
                            visited[j] = 1
            # while 구문 끝나면 연결된 네트워크 하나 찾았으니 누적
            answer += 1
    return answer