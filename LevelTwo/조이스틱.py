def solution(name):
    name=list(name)
    set_A=list('A'*len(name))
    go_str=string.ascii_uppercase
    back_str='A'+go_str[::-1]
    
    cur, cnt=0,0
    go=True
    while set_A!=name:
        if name[cur]!='A':
            go_idx=go_str.index(name[cur])
            back_idx=back_str.index(name[cur])
            cnt+=go_idx if go_idx <= back_idx else back_idx
            set_A[cur]=name[cur]
        if set_A==name:
            return cnt
        if name[cur+1]=='A':
            if len(name[cur+1:])<len(name[cur+1::-1]):
                cur+=1
                cnt+=1
            else:
                cur-=1
                cnt+=1
                go=False
        else:
            if go:
                cur+=1
                cnt+=1
            else:
                cur-=1
                cnt+=1