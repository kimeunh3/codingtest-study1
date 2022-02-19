'''백준 연산자 끼워넣기 14888번

덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수'''

from itertools import permutations

n = int(input())
num_list = list(map(int, input().split()))
oper_list = list(map(int, input().split()))
o = ['+', '-', '*', '/']
operators = []

for i, oper in enumerate(oper_list):
    for _ in range(oper):
        operators.append(o[i])

oper_permu = set(permutations(operators, len(operators))) # 중복 제거

result_list = []
for op_list in oper_permu: # op 연산 조합 리스트
    result_num = num_list[0]
    for i in range(len(op_list)):
        if op_list[i] == '+':
            result_num += num_list[i+1]
        elif op_list[i] == '-':
            result_num -= num_list[i+1]
        elif op_list[i] == '*':
            result_num *= num_list[i+1]
        else:
            if result_num < 0:
                result_num = -(abs(result_num) // num_list[i+1])
            else:
                result_num = result_num // num_list[i+1]
    result_list.append(result_num)

print(max(result_list))
print(min(result_list))