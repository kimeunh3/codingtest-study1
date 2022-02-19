def DFS_BACK(depth, max, start, length, list) :
    if depth == length :
        if start <= max and start >= 0 :
            global curmax
            if curmax < start :
                curmax = start

    else :
        tmp = start
        start = start + volume[depth]
        if start >= 0 and start <= max :
            DFS_BACK(depth + 1, max, start, length, list)
        start = tmp
        start = start - volume[depth]
        if start >= 0 and start <= max :
            DFS_BACK(depth + 1, max, start, length, list)
        start = tmp

List = list(map(int, input().split()))
max = List[2]
start = List[1]
length = List[0]
volume = list(map(int, input().split()))
curmax = -1
DFS_BACK(0, max, start, length, volume)
if curmax == -1 :
    print(-1)
else :
    print(curmax)




