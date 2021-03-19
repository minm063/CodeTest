def solution(phone_book):
    p=sorted(phone_book)

    for s1, s2 in zip(p, p[1:]):
        if s2.startswith(s1):
            return False
    return True