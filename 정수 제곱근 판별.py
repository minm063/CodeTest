def solution(n):
    answer=-1
    if n==1:
        return 4
    for i in range(0,n):
        if i==n**0.5:
            answer=(i+1)**2
            break
    return answer
