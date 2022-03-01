## 풀이  

backtracking으로 풀었습니다.  

모든 경우의 수를 확인해주기 위해 시작하는 숫자 또한 for loop으로 돌려주었고,  
고르지 않은 수들의 list인 not_picked에서 하나를 골라 prev_num과 뺀 값의 절대값을 sum_num에 더해주고, 
고른 숫자를 prev_num으로, 
방금 고른 수를 not_picked에서 제외한 list를 not_picked로 넣어준 뒤 재귀호출을 해줍니다.  

재귀의 종료지점으로는 not_picked의 길이가 0일 때로 해준 뒤,  
현재 sum_num과 전역변수인 max_n을 비교해 더 큰 값을 max_n에 넣어주고 return 해줍니다.  

마지막에는 max_n을 출력해줍니다.  
  
## 코드  
```python
N = int(input())
nums = list(map(int, input().split()))
max_n = 0

def backtrack(sum_num, prev_num, not_picked):
    global max_n

    if not not_picked:
        max_n = max(max_n, sum_num)
        return
    for i in range(len(not_picked)):
        new_num = not_picked[i]
        backtrack(sum_num+abs(prev_num-new_num), new_num, not_picked[:i]+ not_picked[i+1:])

for j in range(N):
    backtrack(0, nums[j], nums[:j]+ nums[j+1:])
print(max_n)
```