def solution(s):
    answer=[]
    s=s[2:-2].split("},{")
    s=sorted(s, key=lambda x:len(x))
    for i in s:
        tmp=i.split(',')
        for j in range(len(tmp)):
            if tmp[j] not in answer:
                answer.append(tmp[j])

    return list(map(int,answer))

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))