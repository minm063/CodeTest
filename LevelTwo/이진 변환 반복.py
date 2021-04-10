def solution(s):
    z_cnt, b_cnt = 0, 0
    while s!='1':
        answer=''
        for i in s:
            if i=='0':
                z_cnt+=1
            else:
                answer+=i
        s=format(len(answer),'b')
        b_cnt+=1
    return [b_cnt,z_cnt]
print(solution("110010101001"))