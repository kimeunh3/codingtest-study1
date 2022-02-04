def solution(N, number):
    answer = 0
    cache = [ set() for _ in range(9) ]
    # cache[num] = [] num개의 N으로 만들 수 있는 수
    # N이 5라면
    for i in range(1, 9):
        cache[i].add(int(str(N)*i)) # 5, 55, 555, 5555, 55555 ...
    for num in range(1, 9):
        for j in range(1, num):
            # +, *는 순서가 바뀌어도 값이 같지만 -와 /는 순서가 바뀌면 값이 달라지기 때문에 반대 순서도 고려를 해주고
            # +, *로 인한 중복은 set으로 처리
            for a in cache[j]:
                for b in cache[num-j]:
                    cache[num].add(a + b)
                    cache[num].add(a - b)
                    cache[num].add(a * b)
                    if b != 0: # division by 0를 예방하기 위함
                        cache[num].add(a // b)
        if number in cache[num]:
            answer = num
            break
    else:
        return -1
    
    return answer