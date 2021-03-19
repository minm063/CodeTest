def solution(n):
    answer = ''
    str = '412'
    while n:
        n,a = divmod(n,3)
        answer = str[a] + answer
        if not a:
            n -= 1
    return answer