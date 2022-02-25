## 프로그래머스 오픈채팅방

### 코드 구현

사용 언어 : **파이썬**

```python
def solution(records):
    answer = []
    # 유저아이디 - 닉네임 형태로 저장될 딕셔너리
    userInfo={}

    for record in records:
        #msg = [Enter/Leave/Change,유저아이디,닉네임]
        msg=record.split(' ')

        # Enter, Change인 경우 아이디-닉네임 초기화
        if len(msg)>2:
            userInfo[msg[1]]=msg[2]
        # Enter, Leave인 경우 채팅방 메세지를 출력해줘야 하므로 answer에 [1/0,아이디] 형태로 삽입
        if msg[0]=='Enter':
            answer.append([1,msg[1]])
        elif msg[0]=='Leave':
            answer.append([0,msg[1]])

    # records를 모두 확인한 후 유저아이디-닉네임을 확정짓고 나서
    # answer에 재대로된 채팅방 메세지를 정해진 형태로 저장
    for i in range(len(answer)):
        if answer[i][0]:
            answer[i]=userInfo[answer[i][1]]+"님이 들어왔습니다."
        else:
            answer[i]=userInfo[answer[i][1]]+"님이 나갔습니다."

    return answer
```
