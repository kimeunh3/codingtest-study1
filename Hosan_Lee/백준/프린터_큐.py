Order = int(input())

for i in range(Order) :
    A = input().split()
    B = input().split() # 문서들이 저장되어있는 배열
    num_1 = int(A[0]) # 문서의 총 개수
    num_2 = int(A[1]) # 우리가 찾고자 하는 문서의 정렬 전 번호
    Priority = [] # Queue 구현
    target = list(range(num_1)) # 문서의 번호를 교환하기 위한 배열

    for i in range(len(B)) :
        Priority.append(int(B[i])) # 배열 정수화

    if num_1 == 1 :
        print(1)

    else :
        count = 1
        while len(B) != 0 :

            if max(Priority) == Priority[0] and num_2 == target[0] :
                print(count) # target의 차례가 된 경우에는 count 출력
                break

            else :
                if max(Priority) != Priority[0] :
                    tmp = Priority[0]
                    del Priority[0]
                    Priority.append(tmp)
                    tmp2 = target[0]
                    del target[0]
                    target.append(tmp2)

                else :
                    del Priority[0]
                    count = count + 1
                    del target[0]