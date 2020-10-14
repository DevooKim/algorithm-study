'''
1. arr를 1차배열(flat)로 만든다.
2. tmp에 flat[i : i+(al//2)]를 더한다. (좌측)
    i+=al하고 i < fl까지 반복
3. i = al // 2로 초기화하고 과정2 반복 (우측)

규칙 : [n : n+(al//2)]

풀이방법
재귀, 분할정복(?)
'''
def solution(arr):
    answer = []
    flat = sum(arr, [])
    al, fl = len(arr), len(flat)

    if flat.count(0) == len(flat):
        return [len(flat), 0]
    elif flat.count(1) == len(flat):
        return [0, len(flat)]

    tmp = []
    tmp2 = []
    while al > 1:
        i = 0
        while i < fl:
            tmp += flat[i : i+(al//2)]
            tmp2.append(tmp)
            tmp = []
            i += al
        
        tmp = []
        i = al // 2
        while i < (fl - (al//2)):
            tmp += flat[i : i+(al//2)]
            tmp2.append(tmp)
            tmp = []
            i += al
        print(tmp2)
        break        

    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]) == [4,9])
#print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]) == [10,15])