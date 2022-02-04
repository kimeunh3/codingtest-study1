T = int(input())

for i in range(T) :
    List = input().split()
    Jump = int(List[1])-int(List[0])
    count = 0
    distance = 1 #현재 운항중인 거리
    flag = 2
    number = 0

    while count < Jump :
        number = number + 1
        flag = flag + 1
        count = count + distance
        if flag % 2 == 0 :
            distance = distance + 1

    print(number)
