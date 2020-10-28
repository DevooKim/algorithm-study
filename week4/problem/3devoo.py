import collections

#내 풀이(미완성)
def solution(bridge_length, weight, truck_weights):
    answer = 0
    #다리 위의 트럭 = 스택
    #stack에 index
    #시간 리스트 별도?(다리 길이만큼)
    truck_weights = collections.deque(truck_weights)
    stack = []
    time = [0] * len(truck_weights)
    i, arrive = 0, 0
    while arrive < len(truck_weights):
        if stack:
            for t in range(len(time)):
                if time[t] == bridge_length + 1:
                    answer += time[t]
                    print(stack)
                    stack.pop(0)
                    arrive += 1
                elif time[t] != 0:
                    time[t] += 1
        if sum(stack) + truck_weights[i] <= weight and i <= len(truck_weights):
            stack.append(truck_weights[i])
            time[i] += 1
            i += 1
        #print(stack)
    return answer

def solution2(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length
    sum_queue = 0

    while q:
        print(q)
        time += 1
        sum_queue -= q.pop(0)

        if truck_weights:
            if truck_weights[0] + sum_queue <= weight:
                sum_queue += truck_weights[0]
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return time

#print(solution(2, 10, [7,4,5,6]))
#print(solution2(2, 10, [7,4,5,6]))
#print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
print(solution2(4, 100, [10,10,10,10,10,10,10,10,10,10]))