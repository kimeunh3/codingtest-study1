
# 숫자 합의 경우의 수 다 찾아서 리스트에 넣고 그 합이 target값과 같은 경우 찾기 

def solution(numbers, target):
   
    arr = [0]   
    for i in numbers:
        case = []    
        for j in arr:   
            case.append(j + i)   
            case.append(j - i)   
        arr = case               
    
    answer = 0
    for i in arr:               
        if i == target:         
            answer += 1

    return answer

