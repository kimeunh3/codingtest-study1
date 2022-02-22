def solution(record):
    answer = []
    id_dict = {}  # 유저 id와 최종 닉네임을 저장
    # check : record 값

    for check in record:
        word = check.split(" ")
        if word[0] == 'Change' or word[0] == "Enter":
            id_dict[word[1]] = word[2]

    for check in record:
        word = check.split(" ")

        if word[0] == "Enter":
            answer.append(f"{id_dict[word[1]]}님이 들어왔습니다.")
        elif word[0] == "Leave":
            answer.append(f"{id_dict[word[1]]}님이 나갔습니다.")

    return answer
