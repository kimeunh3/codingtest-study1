import collections
import copy


def solution(progresses, speeds):
    answer = collections.deque()
    progresses = collections.deque(progresses)
    speeds = collections.deque(speeds)  # 효율성을 위해 list 대신 deque 사용

    count = 0
    check = 0

    while len(progresses) != 0:
        if count <= len(progresses) - 1:  # 모든 작업은 동시에 하므로 모든 작업을 진행
            progresses[count] += speeds[count]
            count += 1  # 한번씩 작업을 모두 해야하므로 count로 조절
        if count == len(progresses):
            if progresses[0] >= 100:  # 첫번째 작업이 100이 넘는지 확인
                for progress in copy.deepcopy(progresses):  # deque를 사용할때 내용이 변경되면 오류발생 [copy.deepcopy를 사용하여 해결]
                    # 에러내용 [RuntimeError: deque mutated during iteration ]
                    if progress >= 100:
                        check += 1  # 완료된 작업의 수
                        progresses.popleft()  # 작업이 완료되면 deque에서 삭제
                        speeds.popleft()
                    else:
                        break  # 가장 앞의 작업이 모두 진행되지 않았다면 앞으로 돌아가 작업 재게
                answer.append(check)  # 완료된 작업의 수 넣기
            else:
                count = 0
            check = 0  # 완료된 작업 수 초기화
            count = 0

    answer = list(answer)
    return answer
