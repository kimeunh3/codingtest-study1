'''프로그래머스 - 다단계 칫솔 판매'''

def solution(enroll, referral, seller, amount):
    result = [0] * len(enroll) # enroll의 순서 그대로
    
    idx_dic = {key: idx for idx, key in enumerate(enroll)}
    
    for sales_person, price in zip(seller, amount):
        price *= 100
        while True:
            if sales_person == "-" or price < 1:
                break
            next_price = int(price * 0.1)
            result[idx_dic[sales_person]] += price - next_price
            
            sales_person = referral[idx_dic[sales_person]]
            price = next_price
            
    return result