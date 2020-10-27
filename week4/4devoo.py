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

print(solution([2,1,3,2], 2))
print(solution([1,1,9,1,1,1], 0))
#print(solution([1, 1, 1, 1], 3))