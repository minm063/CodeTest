def solution(n):
    start = 1
    cnt=0
    while start<=n:
        tmp=0
        for i in range(start,n+1):
            tmp+=i
            if tmp==n:
                cnt+=1
                break
            if tmp>n:
                break
        start+=1
    return cnt
    
print(solution(15))