def solution(record):
    answer = []
    user = dict()
    new_record = [ r.split() for r in record ]
    
    for i in range(len(record)):
        if new_record[i][0] != "Leave":
            user[new_record[i][1]] = new_record[i][2]
            
    for j in range(len(record)):
        if new_record[j][0] != "Change":
            msg = user[new_record[j][1]]
            if new_record[j][0] == "Enter":
                msg += "님이 들어왔습니다."
            elif new_record[j][0] == "Leave":
                msg += "님이 나갔습니다."
            answer.append(msg)
            
    return answer