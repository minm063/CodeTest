def solution(array, commands):
    answer = []
    ex=[]
    for i in range(len(commands)):
        ex=array[(commands[i][0]-1):commands[i][1]]
        ex.sort()
        answer.append(ex[commands[i][2]-1])
    return answer
