List = input().split()
target = int(List[0])
length = int(List[1])
count = 0
flag = True


while length <= 100 :

        if length % 2 != 0 :
            quotient = int(target / length)
            plus_minus = int(length/2)
            tmpcount = 0
            tmpList = []
            for i in range (quotient-plus_minus, quotient+plus_minus+1) : #기준 quotient 부터 +- plus_minus를 해줘서 합의 범위를 구합니다.
                tmpcount = tmpcount + i
                tmpList.append(i)

            if tmpcount == target :
                if tmpList[0] < 0 :
                    length = length + 1
                    continue
                flag = False
                for i in range(len(tmpList)):
                    print(tmpList[i], end=' ')
                break
            else :
                length = length + 1

        else :
            quotient = int(target / length)
            plus_minus = int(length / 2)
            tmpcount = 0
            tmpList = []
            for i in range(quotient - plus_minus + 1, quotient + plus_minus + 1): #예제의 규칙에서 찾을 수 있습니다.
                tmpcount = tmpcount + i
                tmpList.append(i)

            if tmpcount == target:
                if tmpList[0] < 0 :
                    length = length + 1
                    continue

                flag = False
                for i in range(0, len(tmpList)) :
                    print(tmpList[i], end=' ')
                break
            else:
                length = length + 1

if flag == True :
    print(-1)












