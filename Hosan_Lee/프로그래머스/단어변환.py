from collections import deque


def solution(begin, target, words): #begin 시작단어, target 목표단어, words 단어의 배열.
    if target not in words : #얻으려고 하는 단어가 리스트에 없다면?
        return 0 #어차피 불가능하므로 즉시 0을 return 합니다.
    else : #그렇지 않은 경우 BFS를 실행합니다.

        length = len(words)
        visited = [-1 for _ in range(len(words))]   #방문했는지 확인용 배열 생성
        main = deque()                               #BFS 순회용 deque 생성
        for i in range(len(words)) :
            if helper(begin, words[i]) == True :    #helper 함수는 단어가 한개씩만 다른지 판단해주는 함수입니다. 밑에 구현해 놓았어요
                visited[i] = 1                      #조건에 맞다면 visited[i] 에 1(첫번쨰로 방문함)을 넣어주고, 큐에도 넣어줍니다.
                main.append(i)
                if target == words[i] :             #그리고, 이 단계에서 이미 우리의 target과 같은 경우, 1을 리턴해줍니다.
                    return visited[i]
        while main :                                #그렇지 않을 경우, 평범하게 BFS를 수행합니다. 폴짝폴짝 참고해서 작성하였습니다.
            currnode = main.popleft()               #물론 전위 후위 구분해서 하면 조금 더 빠를 순 있겠지만, 귀찮으니 생략 :)
            for i in range(0, length):
                if visited[i] == -1 and helper(words[currnode], words[i]) == True:
                    visited[i] = visited[currnode] + 1
                    main.append(i)
                    if words[i] == target :
                        return visited[i]

        return 0            #스택이 비었는데도 값에 도달하지 못한경우는 0을 리턴합니다. 사실 위에 이런 예외 케이스들을 미리 처리했으므로
                            #피치못할 Extrem Corner Cases들을 예방하기 위해 추가로 return 값을 달아주는 것이 좋습니다.

def helper(original, modified) :
    count = 0
    for i in range(len(original)) :
        if original[i] != modified[i] :
            count = count + 1
    if count == 1 :
        return True
    else :
        return False


