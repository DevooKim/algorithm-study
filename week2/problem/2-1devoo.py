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