import sys

a, b = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
trees.sort()

start = 0
end = max(trees)
while (start <= end):
    sum = 0
    Mid = (start + end) // 2

    for i in trees:
        if i - Mid > 0:
            sum = sum + i - Mid
    
    if sum == b:
        print(Mid)
        break
    
    elif sum > b:
        start = Mid + 1 
    
    elif sum < b:
        end = Mid - 1 
    
else:
    print(end)
   
    


    
    