def solution(arr):
    answer = []
    l = len(arr)
    arr = sum(arr, [])

    n = 0
    tmp3 = []
    while l > 2:
        tmp2 = []
        for i in range(n, len(arr), l*2):
            tmp = []

            #일정 수 만큼 반복
            tmp += arr[i : i+(l//2)]
            tmp += arr[i+l : i+l+(l//2)]

            tmp2.append(tmp)
        
        print(tmp2)
        n += (l//2)
        print(n)
        if n == l:
            print('---')
            n = 0
            l //= 2

    return answer

solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
#solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])