def solution(s):
    answer = 0
    if len(s) == 1:
        return 0

    for i in range(len(s) - 1):
        for j in range(i, len(s)):         
            tmp = [0]
            sliced = s[i:j+1]
            for m in range(len(sliced) - 1):
                for n in range(m, len(sliced)):
                    if sliced[n] != sliced[m]:
                        tmp.append(n - m)
            answer += max(tmp)
    return answer

print(solution("oo"))