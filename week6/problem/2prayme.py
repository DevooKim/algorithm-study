import re


def solution(s):
    answer = [0, 0]

    while s != '1':
        before_len = len(s)
        s = re.sub('[0]', '', s)
        after_len = len(s)

        answer[0] += 1
        answer[1] += before_len - after_len

        s = '{0:b}'.format(after_len)

    return answer


print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))
