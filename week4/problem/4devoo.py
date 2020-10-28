#최근풀이
def solution(priorities, location):
    answer = 0
    index_list = [i for i in range(len(priorities))]
    if len(priorities) == 1:
        return 1

    while priorities:
        print(priorities)
        if priorities[0] < max(priorities[0:]):
            priorities = priorities[1:] + priorities[:1]
            index_list = index_list[1:] + index_list[:1]
        else:
            answer += 1
            priorities.pop(0)
            if index_list.pop(0) == location:
                return answer
    return answer

#이전풀이
def solution2(priorities, location):
    _hash = [(priorities[x],x) for x in range(len(priorities))]
    q = []

    while _hash:
        max_n = max(_hash)
        tmp = _hash.pop(0)
        if tmp[0] < max_n[0]:   #우선순위 비교
            _hash.append(tmp)   #뒤로 다시 넣어 줌
        else:
            q.append(tmp)       #스택에 추가(순서 파악)

    for i in range(len(q)):
        if q[i][1] == location: #순서 찾기
            return i+1

#print(solution([2,1,3,2], 2))
#print(solution2([2,1,3,2], 2))
#print(solution([1,1,9,1,1,1], 0))
print(solution2([1,1,9,1,1,1], 0))
#print(solution([1, 1, 1, 1], 3))