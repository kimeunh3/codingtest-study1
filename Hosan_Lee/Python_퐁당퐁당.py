from collections import deque

def BFSFrog(From, To, Stone, T) :
    Visited = [-1] * T
    Main = deque() # BFS를 위한 배여
    Main.append(From) # currNode 용
    Visited[From] = 0

    while Main :
        currNode = Main.popleft()
        for i in range(currNode, T, Stone[currNode]) : #뒤로 순회
            if Visited[i] == -1 :
                Visited[i] = Visited[currNode] + 1
                Main.append(i)
                if i == To :
                    return Visited[i]

        for i in range(currNode, -1, -Stone[currNode]) : # 앞으로 순회, 현재 돌에 쓰여진 숫자만큼 점프
            if Visited[i] == -1:
                Visited[i] = Visited[currNode] + 1
                Main.append(i)
                if i == To:
                    return Visited[i]

    return -1

T = int(input())
tmpList = input().split()
Stone = list(map(int, tmpList))
tmpList2 = input().split()
From = int(tmpList2[0]) -1
To = int(tmpList2[1]) -1
print(BFSFrog(From, To, Stone, T))


