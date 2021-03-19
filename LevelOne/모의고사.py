def solution(answers):
    cnt1 = cnt2 = cnt3 = 0
    pep=[]
    a=[1,2,3,4,5]
    b=[2,1,2,3,2,4,2,5]
    c=[3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if a[i%5] == answers[i]:
            cnt1+=1
        if b[i%8] == answers[i]:
            cnt2+=1
        if c[i%10] == answers[i]:
            cnt3+=1
    count=max(cnt1,cnt2,cnt3)
    if count==cnt1:
        pep.append(1)
    if count==cnt2:
        pep.append(2)
    if count==cnt3:
        pep.append(3)
    pep.sort()
    return pep
