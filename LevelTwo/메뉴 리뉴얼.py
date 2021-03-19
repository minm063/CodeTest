def solution(orders, course):
    answer = []
    p = []
    for i in course:
        p.append([])
        for j in orders:
            j = ''.join(sorted(list(j)))
            p[-1] +=list(map(''.join, itertools.combinations(list(j), i)))
    tmp=[]
    for j in p:
        tmp.append(collections.Counter(j).most_common())
    print(tmp)
    for k in tmp:
        try:
            while k[0][1] != 1:
                answer.append(''.join(sorted(k[0][0])))
                if len(k) == 1:
                    break
                if k[0][1] == k[1][1]:
                    del k[0]
                    continue
                break
        except IndexError:
            continue
            
    return sorted(answer)