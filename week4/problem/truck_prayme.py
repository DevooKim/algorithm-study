import collections

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_deq, weight_deq = collections.deque(truck_weights), collections.deque()

    cur_weight = 0
    while truck_deq:
        if truck_deq[0]  + cur_weight <= weight:
            cur_weight += truck_deq.popleft()

    return answer

solution(2, 10, [7,4,5,6])
solution(100, 100, [10])
solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])