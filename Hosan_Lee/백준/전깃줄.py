number = int(input())
From = []
To = []
Abs = []
if number == 0 :
    print(0)
if number == 1 :
    print(0)

else :
    dp = [0 for i in range(number)]
    for i in range(number) :
        str = input().split()
        tmp_from = int(str[0])
        From.append(tmp_from)
        tmp_to = int(str[1])
        To.append(tmp_to)
        Abs.append(tmp_from-tmp_to)






