def solution(N, number):
    dp = [None]+[{int(str(N)*i)} for i in range(1, 9)]

    for i in range(1, 9):
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1+op2)
                    dp[i].add(op1-op2)
                    dp[i].add(op1*op2)
                    if op2 != 0:
                        dp[i].add(op1//op2)

        if number in dp[i]:
            return i

    return -1
