def solution(number, k):
    p=[]
    for n in number:
        while p and n>p[-1]:
            if k>0:
                p.pop()
                k-=1
            else:
                break
        p.append(n)
    
    if k>0:
        for i in range(k):
            p.pop()
    return "".join(p)