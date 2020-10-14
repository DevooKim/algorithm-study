def solution(s):
    answer = 0
    if len(s) == 1:
        return 0
    
    for i in range(len(s)-1):
        sliced = s[i]
        r = i
        for j in range(i+1, len(s)):
            l = i
            sliced += s[j]
            print(sliced)
            if s[i] == s[j] and r == 0:
                continue

            if s[i] != s[j]:
                r = j #서로 다른 글자 중 최대 인덱스
            elif s[i] == s[j]:
                while s[l] == s[j] and l < j:
                    l += 1
            #    s[t]와 s[j]가 다를 때 까지 t+=1 후 비교
            diff = max(r - i, j - l)
            print(f'i:{i}, l:{l}, r:{r}, j:{j}')
            print(f'diff:{diff}')
            #answer += (r - l)    
            answer += diff    
    print(f'answer:{answer}')
    return answer
#print(solution("baby") == 9)
#print(solution("abcaa") == 17)
#print(solution("aabaaa") == 22)
print(solution("aaaba") == 13)

'''
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.03ms, 10.2MB)
테스트 4 〉	통과 (0.25ms, 10.2MB)
테스트 5 〉	통과 (2.15ms, 10.3MB)
테스트 6 〉	통과 (11.86ms, 10.3MB)
테스트 7 〉	통과 (105.75ms, 10.1MB)
테스트 8 〉	통과 (972.54ms, 10.4MB)
테스트 9 〉	통과 (8936.17ms, 10.3MB)
테스트 10 〉	실패 (시간 초과)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	실패 (시간 초과)
테스트 13 〉	실패 (시간 초과)
테스트 14 〉	실패 (시간 초과)
테스트 15 〉	실패 (시간 초과)
테스트 16 〉	실패 (시간 초과)
테스트 17 〉	실패 (시간 초과)
'''