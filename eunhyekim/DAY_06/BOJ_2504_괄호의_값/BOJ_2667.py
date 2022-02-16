str1 = input()
stack = []
num = 1
result = 0

for i in range(len(str1)):
    # 열린 괄호 때는 num에 해당 괄호의 수를 곱해주고 stack에 괄호를 넣어준다.
    if str1[i] == '(':
        num *= 2
        stack.append(str1[i])
    elif str1[i] == '[':
        num *= 3
        stack.append(str1[i])
    elif str1[i] == ')': # 닫힌 괄호 ')'
        # 열려있는 괄호가 없거나 마지막 열린괄호와 다를 때는 올바르지 않은 괄호열
        if not stack or stack[-1] == '[':
            result = 0
            break
        # 짝이 되는 열린괄호가 바로 직전에 있었다면 num을 더해준다.
        if str1[i-1] == '(':
            result += num
        # 괄호를 닫아줄 때는 해당 괄호의 수를 다시 나눠준다.
        num //= 2
        stack.pop()
    
    else: # 닫힌 괄호 ']'
        # 열려있는 괄호가 없거나 마지막 열린괄호와 다를 때는 올바르지 않은 괄호열
        if not stack or stack[-1] == '(':
            result = 0
            break
        # 짝이 되는 열린괄호가 바로 직전에 있었다면 num을 더해준다.
        if str1[i-1] == '[':
            result += num
        # 괄호를 닫아줄 때는 해당 괄호의 수를 다시 나눠준다.
        num //= 3
        stack.pop() 

# 아직 닫히지않은 열린 괄호들이 남아있다면 올바르지 않은 괄호열
if stack:
  result = 0

print(result)

