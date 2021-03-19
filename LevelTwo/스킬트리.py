def solution(skill, skill_trees):
    arr = []
    answer = 0

    for i in range(len(skill)):
        arr.append(skill[0:i+1])

    for i in skill_trees:
        p =""
        cnt=0
        for j in i:
            if j in skill:
                p+=j
                cnt+=1
        if p in arr:
            answer+=1
        if cnt==0:
            answer+=1
    return answer