

def DFS_Chess(depth) :

    if depth == size :
        global count
        count += 1
        return

    for i in range(size) :
            check[depth] = i
            if not(a[i] or b[depth+i] or c[depth-i+size-1]) :
                a[i] = b[depth+i] = c[depth-i+size-1] = True
                DFS_Chess(depth + 1)
                a[i] = b[depth + i] = c[depth - i + size - 1] = False

size = int(input())
check = [0] * size
count = 0
a, b, c = [False]*size, [False]*(2*size-1), [False]*(2*size-1) #세로, 대각선 2개 체크용 배열, 속도 향상
DFS_Chess(0)
print(count)