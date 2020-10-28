def solution(prices):
    answer = [0] * len(prices)

    front, back = 0, 1
    cnt = 0
    while front <= len(prices) - 2 and back <= len(prices) - 1:
        cnt += 1
        if prices[front] > prices[back]:
            answer[front], front, back = back - front, front + 1, front + 2
            continue

        if front != len(prices) - 1 and back == len(prices) - 1:
            answer[front] = len(prices) - (front + 1)
            front, back = front + 1, front + 2
            continue
        back += 1
    print(cnt)
    return answer

solution([1,2,3,2,3])