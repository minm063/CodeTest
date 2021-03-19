def solution(s):
    answer = list(s.split(' '))
    sol=[]
    for i in range(len(answer)):
        _=""
        for j in range(len(answer[i])):
            if j%2==0:
                _+=answer[i][j].upper()
            else:
                _+=answer[i][j].lower()
        sol.append(_)
    sol=' '.join(sol)
    return sol
