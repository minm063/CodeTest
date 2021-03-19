def solution(n):
    x=[]
    while n>0:
        n,r = divmod(n,3)
        x.append(r)
    x=''.join(map(str, x))
    answer=int(x, base = 3)
    return answer
