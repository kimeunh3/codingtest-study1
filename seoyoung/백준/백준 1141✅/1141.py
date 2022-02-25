N = int(input())
arr = []
for i in range(N):
    arr.append(input())

arr.sort()
answer = 1
for i in range(len(arr)-1):
    if arr[i+1].startswith(arr[i]) == False:
        answer += 1

print(answer)
