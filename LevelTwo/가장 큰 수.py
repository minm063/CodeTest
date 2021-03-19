def solution(numbers):
    numbers = list(map(str, numbers))
    n=sorted(numbers, key=lambda x:x*3,reverse=True)
    return ''.join(n)