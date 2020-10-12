import sys
def solution(a):
    lowest, _min = sys.maxsize, min(a)
    s = set()

    for i in range(len(a)):
        if a[i] < lowest:
            s.add(a[i])
            lowest = a[i]
        if a[i] == _min:
            break

    lowest = sys.maxsize
    for j in range(len(a) - 1, i, -1):
        if a[j] < lowest:
            s.add(a[j])
            lowest = a[j]
    
    return len(s)

print(solution([9, -1, -5]) == 3)
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]) == 6)