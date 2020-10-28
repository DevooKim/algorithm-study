import collections

def solution(prices):
    answer = [0] * len(prices)

    deq = collections.deque()

    for idx, cur in enumerate(prices):

        if cur > deq[-1]:


        deq.append(idx)

    return answer
solution([1,2,3,2,3])