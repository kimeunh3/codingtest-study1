'''프로그래머스 오픈채팅방

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
'''

def solution(record):

    # 최신 닉네임을 담은 딕셔너리 생성 / {'uid1234': 'Prodo', 'uid4567': 'Ryan'} => 최신 닉네임을 덮어쓰도록
    nickname_dic = {}
    for rec in record:
        if rec[0] in ["E", "C"]: # Enter, Change인 경우
            _, uid, nickname = rec.split()
            nickname_dic[uid] = nickname
    
    # record 순서대로 처리한 메세지를 result 리스트에 담기(Change인 경우는 아무 처리도 하지 않음)
    result = []
    for rec in record:
        uid, action = rec.split()[1], rec.split()[0]
        cur_nickname = nickname_dic[uid]
        if action == "Enter":
            result.append(f"{cur_nickname}님이 들어왔습니다.")
        elif action == "Leave":
            result.append(f"{cur_nickname}님이 나갔습니다.")
    return result