def solution(strings, n):
    answer = []
    arr=[]
    for i in range(len(strings)) :
        arr.append(strings[i][n]+strings[i])
    arr.sort()
    for i in range(len((arr))) :
        answer.append(arr[i][1:])

    return answer
