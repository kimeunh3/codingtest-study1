'''백분 1024번 수열의 합

- 리스트 길이가 홀수일 경우 : 연속된 수들의 평균은 정수
- 리스트 길이가 짝수일 경우 : 연속된 수들의 평균은 실수(0.5인 것에 초점)
'''

def get_arr(n, l):
    result_list = []
    for length in range(l, 101):
        if length % 2 == 1:
            if n % length == 0: # 평균이 int면 나머지는 0이다.
                mean = int(n / length) # 중간값을 기준으로 수열의 범위를 구한다.
                min_num = mean - (length - 1) // 2
                print(min_num)
                if min_num < 0: 
                    continue
                max_num = mean + (length - 1) // 2
                for num in range(min_num, max_num+1):
                    result_list.append(num)
                return ' '.join(map(str, result_list))

        elif length % 2 == 0:
            value = n / length
            if (value - int(value)) == 0.5:
                min_num = int(value - 0.5) - (length // 2 - 1)
                if min_num < 0: 
                    continue
                max_num = int(value + 0.5) + (length // 2 - 1)
                for num in range(min_num, max_num+1):
                    result_list.append(num)
                return ' '.join(map(str, result_list))
    return -1
            

n, l = map(int, input().split())
print(get_arr(n, l))