def solution(s):
    answer = 0
    if len(s) == 1:
        return 0

    for i in range(len(s) - 1):
        tmp, count = [], 0

        for j in range(i, len(s)):
            if not tmp:
                tmp.append(s[j])
                continue
            tmp.append(s[j])
            if tmp[-1] != s[i]:
                count = j - i
            answer += count

    return answer

print(solution("baby"))