def solution(arr):
    answer = []
    s = len(arr) // 2
    
    n = 0
    while s > 0:
        tmp = []

        # (1*4)번씩 반복 1 -> 4 -> 16 -> ...
        for i in range(n, s):
            tmp.append(arr[i][:s]) 

        for i in range(n, s):
            tmp.append(arr[i][s:s+s])

        for i in range(n+s, s+s):
            tmp.append(arr[i][:s])

        for i in range(n+s, s+s):
            tmp.append(arr[i][s:s+s])
        # 결과를 저장
        print(tmp)
        
        s //= 2
    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]) == [4,9])
#print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]) == [10,15])