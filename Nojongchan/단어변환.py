
def spellcheck(a, b):
    dic1 = {}
    dic2 = {}
        
    for i in range(len(a)):
        dic1.setdefault(i, a[i])
        dic2.setdefault(i, b[i])
        
    count = 0
    for i in range(len(a)):
        if dic1[i] != dic2[i]:
            count += 1
        
    if count == 1: 
        return True


from collections import deque

def solution(begin, target, words):
    dq = deque()
    dq.append(begin)
    check = [True] * len(words) # check 리스트
    count = [0] * len(words)
    

    count_dic = {}
    for i in words:
        count_dic.setdefault(i, 1)
    
    count2 = 0
    switch = True
    while dq:        
        now = dq.popleft()
        for i in range(len(words)):
            if spellcheck(now, words[i]) and check[i]: # 스펠체크를 통과하고 그 단어가 아직 한번도 안거친 단어라면
                dq.append(words[i])
                check[i] = False
                if now in count_dic: 
                    count_dic[words[i]] = count_dic[now] + 1
                if  words[i] == target:
                    print(count_dic[words[i]])
                    switch = False
                    break

    if switch: print(0)
            

solution("aaaaaaaaaa", "bbbbbbbbbb", ["aaaaaaaaab", "aaaaaaaabb", "aaaaaaabbb", "aaaaaabbbb", "aaaaabbbbb", "aaaabbbbbb", "aaabbbbbbb", "aabbbbbbbb", "abbbbbbbbb",
"aaaabaaaaa", "aaaabaaaba", "aaabbaaaab", "babaaabaab", "abbaaaabbb", "bbaabbbbaa", "babaabbbbb", "abbbbbbabb", "babbbbbbbb", "bbabbbbbbb", "bbbabbbbbb", "aaaaaaaaaa", "bbbbbbbbbb"] )





 




    
    
