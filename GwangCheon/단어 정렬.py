count_num = int(input())

save_word = []  # 입력 받는 문자를 저장할 리스트

for i in range(count_num):
    save_word.append(input())

"""
중복문자를 제거하기 위해 set 사용 이때, set 을 사용하면 타입이 set 으로 바뀌기 때문에 
list 로 다시 바꿔주기 위해 list 로 형변환 시켜준다.
"""
save_word = list(set(save_word))

save_word.sort()  # sort 를 사용해서 사전 순으로 정렬
save_word.sort(key=len)  # sort 에 옵션 key=len 을 추가하여 문자열 길이 순으로 정렬

for i in save_word:
    print(i)
