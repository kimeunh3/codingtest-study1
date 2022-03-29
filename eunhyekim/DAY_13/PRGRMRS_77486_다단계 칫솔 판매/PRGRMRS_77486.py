from collections import defaultdict

def recur(idx, person, referred, price):
    global answer
    if referred[person] == "-" or price == 0:
        answer[idx[person]] += price-(price//10)
        return
    ref = referred[person]
    percent = price//10
    answer[idx[person]] += price-percent
    recur(idx, ref, referred, percent)

def solution(enroll, referral, seller, amount):
    global answer
    idx = { enroll[i]: i for i in range(len(enroll))}
    referred = {enroll[k]:referral[k] for k in range(len(enroll))}
    answer = [0 for _ in range(len(enroll))]
    sold = defaultdict(list)
    for j in range(len(seller)):
        sold[seller[j]].append(100*amount[j])
    for person, price in sold.items():
        for p in price:
            recur(idx, person, referred, p)

    return answer