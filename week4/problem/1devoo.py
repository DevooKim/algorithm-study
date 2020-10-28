import time
from collections import deque

#이전풀이
def solution(prices):
    start = time.time()
    answer = []
    prices = deque(prices)
    count = 0

    while prices:
        price = prices.popleft()
        days = 0
        for other_price in prices:
            count += 1
            days += 1
            if price > other_price:
                break
        answer.append(days)

    answer[-1] = 0
    print(count)
    print(f'solution: {time.time() - start}')
    return answer

#최근풀이
def solution2(prices):
    start = time.time()
    answer = [0] * len(prices)
    stack = []

    for i, v in enumerate(prices):
        while stack and v < prices[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    #남은 스택 처리
    for s in stack:
        answer[s] = len(prices) - 1 - s
    print(count)
    print(f'solution2: {time.time() - start}')
    return answer

#print(solution([1,2,3,2,3,1,2,3,2,3,1,2,3,2,3,1,2,3,2,3,1,2,3,2,3]))
print(solution2([1,2,3,2,3,1,2,3,2,3,1,2,3,2,3,1,2,3,2,3,1,2,3,2,3]))
