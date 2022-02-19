## 풀이  


  
## 코드  
```python
import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
input_opers = list(map(int, input().split()))
min_n, max_n = 1000000000, -1000000000

opers = []
for i in range(len(input_opers)):
    opers.extend([i for _ in range(input_opers[i])])

def operate(oper, num1, num2):
    if oper == 0:
        return num1 + num2
    elif oper == 1:
        return num1 - num2
    elif oper == 2:
        return num1 * num2
    else:
        return int(num1 / num2)

def backtrack(num, nums, opers):
    global min_n, max_n
    if len(opers) == 0:
        # print(num, num)
        min_n, max_n = min(min_n, num), max(max_n, num)
        # print("-----------------------------")
        return
    for i in range(len(opers)):
        if nums[0] == 0 and opers[i] == 3:
            continue
        # print(num, nums, opers)
        backtrack(operate(opers[i], num, nums[0]), nums[1:], opers[:i]+opers[i+1:])

backtrack(nums[0], nums[1:], opers)
print(max_n, min_n, sep="\n")
```