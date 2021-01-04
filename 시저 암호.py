def solution(s, n):
    answer = []
    
    for i in s:
        i=ord(i)
        if i==32:
            answer.append(chr(i))
            continue
        if i>=65 and i<=90:
            if i+n>90:
                answer.append(chr(i-26+n))
            else:
                answer.append(chr(i+n))
        if i>=97 and i<=122:
            if i+n>122:
                answer.append(chr(i-26+n))
            else:
                answer.append(chr(i+n))
    answer=''.join(answer)
    return answer
