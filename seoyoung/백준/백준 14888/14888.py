N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
maxNum = -1e9
minNum = 1e9


def dfs(depth, num, plus, minus, mul, div):
    global maxNum, minNum
    if depth == N:
        maxNum = max(num, maxNum)
        minNum = min(num, minNum)
        return

    if plus:
        dfs(depth+1, num+nums[depth], plus-1, minus, mul, div)
    if minus:
        dfs(depth+1, num-nums[depth], plus, minus-1, mul, div)
    if mul:
        dfs(depth+1, num*nums[depth], plus, minus, mul-1, div)
    if div:
        dfs(depth+1, int(num/nums[depth]), plus, minus, mul, div-1)


dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3])
print(maxNum)
print(minNum)
