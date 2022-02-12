def result(tri_list, Size) :
    for i in range(1, Size) :
        for j in range(1, i + 2) : #아까 0을 두개 삽입했기에 i + 1까지 탐색합니다.
            tri_list[i][j] += max(tri_list[i-1][j-1], tri_list[i-1][j])
    return max(tri_list[-1])


Size = int(input())
tri_list = []
for i in range(Size):
    tri_list.append(list(map(int, input().split())))
    tri_list[i].insert(0,0)
    tri_list[i].append(0) #양 끝에 0을 삽입해 따로 index가 0이거나 1일때 처리할 필요 없게 만듭니다.
print(result(tri_list, Size))


