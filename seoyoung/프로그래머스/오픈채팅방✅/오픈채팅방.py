def solution(records):
    answer = []
    userInfo = {}

    for record in records:
        msg = record.split(' ')

        if len(msg) > 2:
            userInfo[msg[1]] = msg[2]
        if msg[0] == 'Enter':
            answer.append([0, msg[1]])
        elif msg[0] == 'Leave':
            answer.append([1, msg[1]])

    for i in range(len(answer)):
        if answer[i][0] == 0:
            answer[i] = userInfo[answer[i][1]]+"님이 들어왔습니다."
        else:
            answer[i] = userInfo[answer[i][1]]+"님이 나갔습니다."

    return answer
