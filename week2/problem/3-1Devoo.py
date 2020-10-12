def solution(a):
    answer = 0
    s = set()
    m = a.index(min(a))

    for i in range(len(a)):
        if i < m:
            s.add(min(a[:i+1]))
        elif i > m:
            s.add(min(a[i:]))
        else:
            s.add(a[i])
    answer = len(s)
    return answer

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]) == 6)
