# 1270번 전쟁 - 땅따먹기

n = int(input())
for i in range(n):
    land = list(map(int, input().split()))
    num, land = land[0], land[1:]

    land_dic = {}
    control = True

    for i in land:
        if i in land_dic:
            land_dic[i] = land_dic[i]+1
            if land_dic[i] > num/2:
                print(i)
                control = False
                break
        else:
            land_dic[i] = 1

    if control:
        print("SYJKGW")
