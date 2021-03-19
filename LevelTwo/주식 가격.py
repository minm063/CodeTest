def solution(prices):
    answer = [0] * len(prices)
    for n, i in enumerate(prices):
        for j in range(n+1, len(prices)):
            answer[n] += 1
            if i > prices[j]:
                break
    return answer