from itertools import permutations

def check(n):
    if n < 2: 
        return False

    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    for k in range(1, len(numbers)+1):
        p = list(map(''.join, permutations(list(numbers), k)))
        for i in list(set(p)):
            if check(int(i)):
                answer.append(int(i))

    answer = len(set(answer))

    return answer