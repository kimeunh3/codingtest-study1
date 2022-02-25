'''백준 접두사 1141번'''

n = int(input())
arr = set([input() for _ in range(n)]) # 중복값은 제거

if not n:
    print(0)
    exit()

result = len(arr) # 결과값은 배열의 길이가 최대값이다
for head_str in arr:
    cnt = 1 # 자기 자신 포함
    for string in arr:
        if head_str == string:
            continue
        if string.startswith(head_str): # head_str이 다른 문자열의 접두어라면, 해당 head_str을 갯수에서 제외
            result -= 1
            break

print(result)