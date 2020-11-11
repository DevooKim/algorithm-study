def solution(a):

    # 스타수열의 조건
    # 길이가 2이상의 짝수 (빈수열 X)
    # 같은 길이끼리의 부분 수열은 교집합인 원소가 1개 이상있어야한다.
    # 인접하는 원소는 같으면 안된다.

    if len(a) == 1:
        return 0

    def dfs(length):
        if length == 1:
            return 0

        start, answer = 0, 0
        while start + length <= len(a) or answer != 0:
            # print(a[start: start+length])

            # 길이에 맞게 자르기
            window = a[start:start+length]

            # 2개씩 나누기
            separated = [window[i:i+2] for i in range(0, len(window), 2)]
            # print(separated)

            # 인접한 것들끼리 같은지 체크
            prev_left, prev_right = -1, -1
            for left, right in separated:
                if left == prev_right or right == prev_left: # 중복값이면

                    if start+length != len(a): # 마지막 윈도우가 아니면 한칸이동
                        start += 1
                        continue

                    return dfs(length // 2) # 마지막 윈도우면 재귀

                prev_left, prev_right = left, right

            # 교집합 체크
            elem, flag = separated[0], 0
            for element in separated[1:]:
                if not elem[0] in element:
                    flag = 1
                    break

            if flag == 1: # 만약 교집합을 못찾았으면
                for element in separated[1:]:
                    if not elem[1] in element: # 교집합이 없으면

                        if start+length != len(a): # 마지막 윈도우 아니면 한칸 이동
                            start += 1
                            continue

                        return dfs(length // 2) #


            return length

    # 일단 최대 길이의 부분집합 구하기
    max_length = 1
    while max_length * 2 < len(a):
        max_length *= 2


    return dfs(max_length)


print(solution([0]))
print(solution([5,2,3,3,5,3]))
print(solution([0,3,3,0,7,2,0,2,2,0]))