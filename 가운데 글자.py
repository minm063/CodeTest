def solution(s):
    slen=len(s)//2
    if len(s) % 2 == 0:
        return s[slen-1:slen+1]
    else:
        return s[slen]
