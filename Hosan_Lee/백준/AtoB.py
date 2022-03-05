Num = input().split()
From = int(Num[0])
To = int(Num[1])
dp = []

if From == 0 or To < From:
    print(-1)
else :
    count = 1
    for i in range(0, To + 1) :

        if i < From :
            dp.append(-1)
        elif i == From :
            dp.append(1)
        elif i < From * 2 :
            dp.append(-1)
        elif i % 2 == 0 and dp[int(i/2)] != -1:
            dp.append(dp[int(i/2)] + 1)
        elif (i - 1) % 10 == 0 and dp[int((i-1)/10)] != -1:
            dp.append(dp[int((i-1)/10)] + 1)
        else :
            dp.append(-1)
print(dp[-1])

