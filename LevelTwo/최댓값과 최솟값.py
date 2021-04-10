def solution(s):
    answer=[]
    s=list(map(int,s.split()))
    answer.append(str(max(s)))
    answer.append(str(min(s)))
    return ' '.join(answer)

print(solution("1 2 3 4"))