import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
min_n, max_n = 1e9, -1e9

def dfs(cnt, res, add, sub, mul, div): 
    global min_n, max_n
    if cnt == N: 
        max_n = max(res, max_n) 
        min_n = min(res, min_n) 
        return 
    if add: 
        dfs(cnt+1, res+nums[cnt], add-1, sub, mul, div) 
    if sub: 
        dfs(cnt+1, res-nums[cnt], add, sub-1, mul, div) 
    if mul: 
        dfs(cnt+1, res*nums[cnt], add, sub, mul-1, div) 
    if div: 
        dfs(cnt+1, int(res/nums[cnt]), add, sub, mul, div-1) 
        

dfs(1, nums[0], add, sub, mul, div) 
print(max_n, min_n, sep="\n")

# import sys

# input = sys.stdin.readline

# N = int(input())
# nums = list(map(int, input().split()))
# input_opers = list(map(int, input().split()))
# min_n, max_n = 1000000000, -1000000000

# opers = []
# for i in range(len(input_opers)):
#     opers.extend([i for _ in range(input_opers[i])])

# def operate(oper, num1, num2):
#     if oper == 0:
#         return num1 + num2
#     elif oper == 1:
#         return num1 - num2
#     elif oper == 2:
#         return num1 * num2
#     else:
#         return int(num1 / num2)

# def backtrack(num, nums, opers):
#     global min_n, max_n
#     if len(opers) == 0:
#         # print(num, num)
#         min_n, max_n = min(min_n, num), max(max_n, num)
#         # print("-----------------------------")
#         return
#     for i in range(len(opers)):
#         if nums[0] == 0 and opers[i] == 3:
#             continue
#         # print(num, nums, opers)
#         backtrack(operate(opers[i], num, nums[0]), nums[1:], opers[:i]+opers[i+1:])

# backtrack(nums[0], nums[1:], opers)
# print(max_n, min_n, sep="\n")