def solution(n):
    answer = 0
    ternary = []

    while n > 0:
        n, tmp = divmod(n, 3)
        ternary.append(tmp)

    print(f'ternary: {ternary}')
    t, i = 1, len(ternary)
    while i > 0:
        i -= 1
        print(f'step: {t * ternary[i]}')
        answer += (t * ternary[i])
        t *= 3

    return answer

print(solution(45) == 7)
#print(solution(125) == 229)