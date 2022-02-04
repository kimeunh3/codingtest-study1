def solution(name):
    answer = 0
    ptr = 0 #현재 가리키고 있는 문자의 인덱스, 0부터 시작
    checked = [False] * len(name)

    for i in range(len(name)) :
        if name[i] == 'A' :
            checked[i] = True

    else :
        while False in checked :
         if checked[ptr] == True :
            tmp = move(checked, ptr)
            answer += tmp[0]
            ptr = tmp[1]
         answer += changeChar(name[ptr])
         checked[ptr] = True
        return answer

def changeChar(char) :
    return min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

def move(checked, ptr) :
    result = []
    tmp = ptr
    tmp2 = ptr
    count = 0
    count2 = 0
    while checked[tmp] == True : #뒤로 갈 때
        if tmp == len(checked) - 1 :
            count += 1
            tmp = 0 #맨 뒤면 커서 맨 앞으로
        else :
            tmp += 1
            count += 1
    while checked[tmp2] == True : #앞으로 갈 때
        if tmp2 == 0 :
            count2 += 1
            tmp2 = len(checked) - 1 #맨 앞이면 커서 맨 뒤로
        else :
            tmp2 -= 1
            count2 += 1

    if count2 > count :
        result.append(count)
        result.append(tmp)
    elif count2 < count :
        result.append(count2)
        result.append(tmp2)
    elif count2 == count :
        tmp_count = tmp
        tmp_count2 = tmp2
        ab = 0
        bc = 0
        while checked[tmp_count] == False :
            ab += 1
            tmp_count += 1
            if tmp_count >= len(checked) - 1:
                break
        while checked[tmp_count2] == False :
            bc += 1
            tmp_count2 -= 1
            if tmp_count <= 0:
                break
        if bc < ab :
            result.append(count2)
            result.append(tmp2)
        else :
            result.append(count)
            result.append(tmp)
    return result


result = solution(input())
print(result)