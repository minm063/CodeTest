def solution(n):
    answer = 0
    p=n+1
    bn=bin(n)[2:]
    while True:
        if bn.count('1')==bin(p)[2:].count('1'):
            break
        p+=1
    return p

print(solution(78))