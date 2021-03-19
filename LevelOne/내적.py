def solution(a, b):
#내적은 a[0]*b[0] + a[1]*b[1] + ...
    answer=0
    for i, j in zip(a, b):
        answer+=i*j
    return answer
