'''프로그래머스 N으로 표현'''

def solution(N, number):
    dp = [None] + [{int(str(N)*i)} for i in range(1, 9)]
    for i in range(1, 9):
        for j in range(1, i):
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2:
                        dp[i].add(num1 // num2)

        if number in dp[i]:
            return i

    return -1