def solution(p):
    answer=""
    u, v = "", ""

    if len(p)==0:
        return answer

    for i in range(2,len(p)+1,2):
        if p[0:i].count("(") == p[0:i].count(")"):
            u=p[0:i]
            v=p[i:]
            break

    if u[0]=="(":
        answer=u+solution(v)
    else:
        answer="("+solution(v)+")"
        u=u[1:-1]
        for i in range(len(u)):
            if u[i]=="(":
                answer+=")"
            else:
                answer+="("

    return answer