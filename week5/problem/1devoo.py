def solution(n, delivery):
    answer = ''
    #0: 모름. 1: 있음, 2: 없음
    stock = [0] * n
    delivery = list(sorted(delivery, key=lambda x: x[2], reverse=True))

    for stuff in delivery:
        if stuff[2] == 1:
            stock[stuff[0] - 1] = 1
            stock[stuff[1] - 1] = 1
        else:
            #판단
            if stock[stuff[0] - 1] == 1:
                stock[stuff[1] - 1] = 2
            elif stock[stuff[1] - 1] == 1:
                stock[stuff[0] - 1] = 2
    
    for s in stock:
        if s == 0:
            answer += '?'
        elif s == 1:
            answer += 'O'
        if s == 2:
            answer += 'X'
    return answer

#print(solution(6, [[1,3,1],[3,5,0],[5,4,0],[2,5,0]]))
print(solution(	7, [[5, 6, 0], [1, 3, 1], [1, 5, 0], [7, 6, 0], [3, 7, 1], [2, 5, 0]]))