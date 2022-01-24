T = int(input())

for i in range(T) :
    tmplist = input().split()
    Conquer = int(int(tmplist[0])/2)
    Soldier_Count = {}
    for j in range(1, len(tmplist)) :
        if tmplist[j] not in Soldier_Count :
            Soldier_Count[tmplist[j]] = 1
        else :
            Soldier_Count[tmplist[j]] = Soldier_Count[tmplist[j]] + 1
    listA = Soldier_Count.values()
    listB = Soldier_Count.keys()
    if max(Soldier_Count.values()) <= Conquer :
        print("SYJKGW")
    else :
        print(max(Soldier_Count ,key= Soldier_Count.get))
