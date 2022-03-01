N = int(input())
nums = list(map(int, input().split()))
max_n = 0

def backtrack(sum_num, prev_num, excluded):
    global max_n

    if not excluded:
        max_n = max(max_n, sum_num)
        return
    for i in range(len(excluded)):
        new_num = excluded[i]
        backtrack(sum_num+abs(prev_num-new_num), new_num, excluded[:i]+ excluded[i+1:])

for j in range(N):
    backtrack(0, nums[j], nums[:j]+ nums[j+1:])
print(max_n)