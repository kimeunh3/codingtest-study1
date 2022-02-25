from itertools import permutations

def sum_all(X) :
    result = 0
    for i in range(len(X)-1) :
        result += abs(X[i] - X[i+1])
    return result

T = int(input())
num_list = list(map(int, input().split()))
result = -100000000
for X in list(permutations(num_list)) :
    tmp_result = sum_all(X)
    if tmp_result > result :
        result = tmp_result
print(result)




