def solution(s):
    answer = 0
    if len(s) == 1:
        return 0

    for i in range(len(s) - 1):
        for j in range(i, len(s)):         
            sliced = s[i:j+1]
            _max = 0
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
                        #_max = _max < n-m and n-m or _max
                        _max = max(n-m, _max)
                        break
            answer += _max
            
    return answer

print(solution("baby"))
print(solution("abcaa"))
print(solution("aabaaa"))
print(solution("aaaba"))


'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.10ms, 10.3MB)
테스트 4 〉	통과 (1.83ms, 10.2MB)
테스트 5 〉	통과 (31.29ms, 10.2MB)
테스트 6 〉	통과 (813.26ms, 10.2MB)
테스트 7 〉	실패 (시간 초과)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	실패 (시간 초과)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	실패 (시간 초과)
테스트 13 〉	실패 (시간 초과)
테스트 14 〉	실패 (시간 초과)
테스트 15 〉	실패 (시간 초과)
테스트 16 〉	실패 (시간 초과)
테스트 17 〉	실패 (시간 초과)
'''