import math

def solution(progresses, speeds):
    p=[] # 배포 가능일
    answer=[] # 배포일
    for pg, sp in zip(progresses, speeds):
        p.append(math.ceil((100-pg)/sp))
    
    prev=p[0]
    for i in p:
        if i>prev:
            answer.append(p.index(i)-p.index(prev))
            prev=i
    answer.append(len(p)-p.index(prev))
    return answer