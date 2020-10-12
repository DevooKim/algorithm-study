from functools import reduce

def solution(n):
    answer = []
    matrix = [[0] * n for i in range(n)]

    i, j, count = -1, 0, 1
    while n > 0:
        for _ in range(n):
            i += 1
            matrix[i][j] = count
            count += 1
        n -= 1
        
        for _ in range(n):
            j += 1
            matrix[i][j] = count
            count += 1
        n -= 1

        for _ in range(n):
            i -= 1
            j -= 1
            matrix[i][j] = count
            count += 1
        n -= 1

    matrix = list(filter(lambda x: x != 0, reduce(lambda x, y: x + y, matrix, [])))
    return matrix

print(solution(4) == [1,2,9,3,10,8,4,5,6,7])
print(solution(5) == [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9])
print(solution(6) == [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11])

        