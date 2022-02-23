## 풀이

우선, 바뀐 닉네임을 저장해주기 위해 for loop을 돌려 user라는 dictionary에 유저 아이디에 따른 닉네임을 저장해주었습니다.  

그 이후로는 닉네임을 바꾸었을 때는 따로 메세지를 출력하지 않기 때문에 **제외**해준 뒤,  
해당 **유저 아이디에 따른 닉네임**을 msg에 저장한 뒤,  
Enter라면 "님이 들어왔습니다."를,  
Leave라면 "님이 나갔습니다."를 더해준 뒤 answer에 append 해주었습니다.  

## 코드
```python
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
```
