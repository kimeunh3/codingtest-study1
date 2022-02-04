from types import coroutine


arr = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

# i = 로우(arr의 길이, 각각의 학생들)
# j = 칼럼(학생이 가지는 각각의 속성의 종류)


set = set()
count = 0
for j in range(len(arr[0])):
    for i in range(len(arr)):
        set.add(arr[i][j])

    if len(set) == len(arr):
        count += 1
        set.clear()

print(count)



