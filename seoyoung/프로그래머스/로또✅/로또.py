def solution(lottos, win_nums):
    unvisible_nums=0
    grade=7
    
    for num in lottos:
        if num==0:
            unvisible_nums+=1
        elif num in win_nums:
            grade-=1
    
    max_grade=grade-unvisible_nums if grade-unvisible_nums<6 else 6
    min_grade=grade if grade<6 else 6
    
    return [max_grade, min_grade]