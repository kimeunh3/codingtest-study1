## 풀이

일단 바꿀 알파벳을 고르기 위해 커서를 옮기는 가로 움직임(hori_move)과 알파벳을 바꾸는 세로 움직임(vert_move)로 나눠줬습니다.  

hori_move는 첫 번째 위치에서 오른쪽으로만 옮기는 경우로 초기화해주었습니다. 만약 이름이 A로 끝난다면 끝부분까지 옮기지 않아도 되기 때문에 끝에서부터 A의 개수를 세어주어 hori_move에서 제외해주었습니다.

vert_move는 각 알파벳마다 'A'에서 시작하는 경우와 'Z'에서 시작하는 경우 두 가지 중 적은 수로 저장해줍니다.

hori_move에는 세 가지 경우가 있습니다.  
만약 A가 중간에 많이 몰려있을 경우, 돌아가는 것이 더 적은 움직임일 수 있기 때문에 확인해줘야 합니다.

1. 돌아가지 않고 오른쪽으로만 옮긴 경우 (앞에서 hori_move에 초기화해준 값)
2. 오른쪽으로 옮겼다가 첫 A를 만나면 왼쪽으로 되돌아가 뒤에서 마지막 A까지 가는 경우
	- "ABAAAAAAAAABB"
		- 1번의 경우: 12
		- 2번의 경우: **4**
		- 3번의 경우: 5
3. 뒤로 먼저 간 뒤 마지막 A를 만나면 다시 오른쪽으로 되돌아가 앞에서 다시 첫 A까지 가는 경우
	- "BBBBAAAABA"
		- 1번의 경우: 9
		- 2번의 경우: 8
		- 3번의 경우: **7** 

첫 번째의 경우 이미 초기화를 해주었고, 두 번째와 세 번째에서는 아래와 같이 찾아줍니다.  

 - i = 여태까지 온 길
 - (len(name) - midA) = 뒤에서부터 가야하는 길
이라고 한다면 두 번째는 여태까지 온 길을 왕복할 것이고, 세 번째는 뒤에서부터 가야하는 길을 왕복할 것이므로,
 - 두 번째 경우 =  i*2 + (len(name) - midA)
 - 세 번째 경우 = (len(name) - midA)*2 + i
가 됩니다. 세 가지 모두의 경우 중 가장 작은 수로 update해줍니다.  

마지막으로는 hori_move와 vert_move를 더한 값을 return 해줍니다.


## 코드
```python
def solution(name):
    # 가로 움직임
    hori_move = len(name)-1
    # 끝에서부터 A의 개수를 제외
    while name[hori_move] == 'A' and hori_move > 0:
        hori_move -= 1
    # 세로 움직임
    vert_move = 0
    for i, char in enumerate(name):
        vert_move += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 중간에 있는 A 중 마지막 A의 위치
        midA = i + 1
        while  midA < len(name) and name[midA] == 'A':
            midA += 1
        # 아래의 세 가지의 경우를 보고 가장 적은 움직임 고르기
        # 1. hori_move = 돌아가지 않고 앞으로만 간 경우
        # 2. i*2 + (len(name) - midA) = 앞으로 가다가 뒤로 다시 돌아가는 경우
        # 3. (len(name) - midA)*2 + i = 뒤로 먼저 간 뒤 앞으로 다시 돌아오는 경우
        hori_move = min(hori_move, i*2 + (len(name) - midA), (len(name) - midA)*2 + i)
    
    # 가로와 세로 움직임 모두 더한 값을 return
    return hori_move + vert_move
```