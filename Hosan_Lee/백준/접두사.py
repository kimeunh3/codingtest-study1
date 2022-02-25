T = int(input());
word_list = []
for i in range(T) :
    word_list.append(input())
word_list.sort(key=lambda x: len(x)) #문자의 길이별로 정렬
count = 1
for i in range(T-1) :
    flag = False
    length = len(word_list[i])
    for j in range(i+1, T) :
        if word_list[i] == word_list[j][0:length] :
            flag = True
            break
    if flag == False :
        count += 1
print(count)