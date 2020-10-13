def solution(s):
    answer = 0
    if len(s) == 1:
        return 0

    for i in range(len(s) - 1):
        for j in range(i, len(s)):         
            sliced = s[i:j+1]
            _max, l, r= 0, 0, len(sliced) - 1
            '''
            for m in range(len(sliced) - 1):
                for n in range(m, len(sliced)):
                    if sliced[n] != sliced[m]:
                        _max = _max < n-m and n-m or _max
            answer += _max
            '''

            '''
            뒤에서부터 한쪽만 탐색 -> 아름다운 문자가 앞쪽이 더 가까울 수가 있다.
            for m in range(len(sliced)-1, 0, -1):
                if sliced[0] != sliced[m]:
                    answer += m
                    break
            '''

            #브루트포스 역순
            for m in range(len(sliced) - 1):
                for n in range(len(sliced)-1, m, -1):
                    if sliced[n] != sliced[m]:
                        _max = _max < n-m and n-m or _max
                        break
            answer += _max
            
    return answer

print(solution("baby"))