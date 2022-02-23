idDict = dict()
def solution(record):
    answer = []
    Log = []
    for i in record:
        command = i.split(" ")
        if command[0] == "Leave":
            Log.append([command[1], "님이 나갔습니다."])
        elif command[0] == "Enter":
            idDict[command[1]] = command[2]
            Log.append([command[1], "님이 들어왔습니다."])
        elif command[0] == "Change":
            idDict[command[1]] = command[2]
    for log in Log:
        answer.append(idDict[log[0]] + log[1])
    return answer