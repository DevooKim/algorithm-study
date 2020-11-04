# 1. 일단 재고가 남은 녀석들 부터 채운다.
# 2. 재고가 남은 녀석이 있는데 배송이 불가능인 것들을 X로 채운다
# 그리고 나머지는 ? 로 리턴

def solution(n, delivery):
    shipped = ['?'] * n

    clone = delivery
    for ship in clone:
        if ship[2] == 1:
            shipped[ship[0] - 1], shipped[ship[1] - 1] = 'O', 'O'
            delivery.remove(ship)


    clone = delivery
    for ship in clone:
        left, right = ship[0] - 1, ship[1] - 1
        if shipped[left] == 'O' and shipped[right] == '?':
            shipped[right] = 'X'
        elif shipped[left] == '?' and shipped[right] == 'O':
            shipped[left] = 'X'

    return ''.join(shipped)

print(solution(6, [[1,3,1],[3,5,0],[5,4,0],[2,5,0]]))