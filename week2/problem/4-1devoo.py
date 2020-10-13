def solution(s):
    answer = 0
    if len(s) == 1:
        return 0
    
    #투포인터와 같은 문제 왼쪽에서 더 가까운 경우 못찾음(abcaa)
    for i in range(len(s)-1):
        sliced = s[i]
        l = i 
        for j in range(i+1, len(s)):
            sliced += s[j]
            print(sliced)
            if s[i] == s[j] and l == 0:
                continue
            if s[i] != s[j]:
                l = j #서로 다른 글자 중 최대 인덱스
            #elif s[i] == s[j]:
            #    t = i
            #    s[t]와 s[j]가 다를 때 까지 t+=1 후 비교
            print(l, i)
            answer += (l - i)    
            
    return answer
#print(solution("abcaa"))
print(solution("aabcaaa"))