'''백준 감소하는 수 1038번'''

import sys

def get_decreasing_number(n):
    cnt = 0
    num = 1
    while True:
        str_num = str(num)
        flag = True
        if len(str_num) == 1:  # 길이가 1이면 무조건 감소하는 수
            pass
        else:
            for i in range(1, len(str_num)):
                if int(str_num[i]) < int(str_num[i-1]): # 감소하는 수인 경우
                    continue
                else: # 어떤 한 자리라도 감소하는 수의 조건을 만족하지 못하는 경우
                    start = str_num[:i-1]
                    mid = str(int(str_num[i-1]) + 1)
                    end = '0' + str_num[i+1:]
                    num = int(start + mid + end) # 522이면 530 전까지 수는 모두 감소하는 수가 아니므로 숫자를 522->530으로 만든다.
                    flag = False
                    break
        if flag: # flag가 True라는 것은 감소하는 수라는 것.
            cnt += 1
            if cnt == n:
                return num
            num += 1 # 현재 숫자가 감소하는 수일 때 +1을 해줘서 다음 수로 넘어간다.

n = int(sys.stdin.readline())
if n >= 1023:  # 1022: 9876543210
    print(-1)
elif n == 0:
    print(0)
else:
    print(get_decreasing_number(n))