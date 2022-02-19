from itertools import permutations
import sys
N = int(sys.stdin.readline())
operations = ['+', '-', '*', '/']
number_input = list(map(int, sys.stdin.readline().split()))
operations_input = list(map(int, sys.stdin.readline().split()))  # + - * / 순서대로 숫자를 입력

operation_list = []

for i in range(4):
    for j in range(operations_input[i]):
        operation_list.append(operations[i])
print(operation_list)
operation_list = list(set(permutations(operation_list)))
# 가능한 조합을 모두 사용하기 위해 permutations를 사용하여 조합들을 list에 저장
# 이때 set을 사용하지 않고 중복된 조합들도 사용하게 할 시 시간초과가 뜨므로 set을 통해 중복은 제거해준다.
answer = []

for i in operation_list:
    result = number_input[0]
    for j in range(N - 1):
        if i[j] == '+':
            result += number_input[j + 1]
        elif i[j] == '-':
            result -= number_input[j + 1]
        elif i[j] == '*':
            result *= number_input[j + 1]
        else:
            if result // number_input[j + 1] < 0:
                result = -(-result // number_input[j + 1])
            else:
                result = result // number_input[j + 1]

    answer.append(result)
print(max(answer))
print(min(answer))
