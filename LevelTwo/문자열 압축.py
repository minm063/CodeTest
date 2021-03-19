def solution(s):
    answer = 1000
    if len(s)<=1:
        return len(s)
    for i in range(1,(len(s)//2)+1):
        string=''
        j=0
        cnt=1
        while j < len(s):
            if s[j:j+i]==s[j+i:j+i+i]:
                cnt+=1
            elif cnt<=1:
                string+=s[j:j+i]
                cnt=1
            else:
                string+=str(cnt)+s[j:j+i]
                cnt=1
            j+=i
        if len(string)<answer:
            answer=len(string)
    return answer