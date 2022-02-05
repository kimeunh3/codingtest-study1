def solution(name):
    
    dic = {
        'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 
        'L':11, 'M':12, 'N':13, 'O':12, 'P':11, 'Q':10, 'R':9, 'S':8, 'T':7, 'U':6, 'V':5,
        'W':4, 'X':3, 'Y':2, 'Z':1 
    }

    # 문자에 'A'가 없을 경우
    arr = [name[i] for i in range(len(name))]
    if 'A' not in arr:
        answer = [dic[j] for j in arr]
        return sum(answer)+len(arr)-1

    # 문자에 'A'가 있을 경우 
    if 'A' in arr:
        answer = [dic[j] for j in arr]
        count = 0
        Q = []
        
        for i in range(len(arr)):
            if arr[i] != 'A':
                Q.append(count)
                count += 1
            else:
                count += 1 

        if len(Q) == 0: # 'A'가 아닌 원소가 없으면 그냥 0이 리턴
            return 0
        
        elif len(Q) == 1:  # 'A'가 아닌 원소가 하나인경우 
            if Q[0] <= len(arr) - Q[0]:  # 정방향으로 가는게 빠른지 역방향으로 가는게 빠른지 비교
                return Q[0] + sum(answer)
                
            else: 
                return len(arr) - Q[0] + sum(answer)

        if len(arr) - Q[len(Q)-1] < Q[0]:   # 첫번째 'A'아닌 원소가 역방향으로 갈 경우 더 빠르게 만난다면 
            Q.sort(reverse=True)            # 역순으로 먼저 가고 정방향으로 방향을 바꿔 가기로함
            Q = [len(arr)- i for i in Q]
                
            for j in range(1, len(Q)):
            
                if Q[j] - Q[j-1] >= Q[j-1] + (len(arr) - Q[j]): 
                    return ( Q[j-1] + Q[j-1] + (len(arr) - Q[j]) + sum(answer) ) 

                elif j == len(Q) - 1:
                    return (Q[j] + sum(answer) )
               
        
        else:    

            for j in range(1, len(Q)):
            
                if Q[j] - Q[j-1] >= Q[j-1] + (len(arr) - Q[j]): # 다음 원소로 정방향으로 갈 떄 드는 비용이 역순으로 가는 비용보다 크다면
                    return ( Q[j-1] + Q[j-1] + (len(arr) - Q[j]) + sum(answer) ) # 다음 원소까지 역방향으로 가버림. (그사이에 다른 원소들을 통과) 

                elif j == len(Q) - 1:
                    return (Q[j] + sum(answer) )
               

print(solution("AABBBAAAABB"))


