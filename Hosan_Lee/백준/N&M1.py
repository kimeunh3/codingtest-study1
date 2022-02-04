

def DFS_Back(depth, N, M, start) :
    if depth == M :
        print(' '.join(map(str, out)))
        return

    for i in range(start, N) :
            out.append(i + 1)
            DFS_Back(depth+1, N, M, i)
            out.pop()



N, M = map(int, input().split())
out = []
DFS_Back(0, N, M, 0)








