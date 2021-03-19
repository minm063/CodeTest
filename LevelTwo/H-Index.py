def solution(citations):
    citations.sort()
    h, k, answer = 0, 0, 0
    for i in range(0, citations[-1]+1):
        h=sum(j>=i for j in citations)
        k=sum(j<=i for j in citations)
        if h>=i and k<=i:
            if i>answer:
                answer=idx
    if citations[0]>=len(citations):
        answer=len(citations)
    return answer