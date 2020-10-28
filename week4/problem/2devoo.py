import math
import time
def solution(progresses, speeds):
    start = time.time()
    answer, stack = [], []
    #progresses = list(map(lambda x: 100 - x, progresses))
    #progresses = [math.ceil(p / s) for p, s in zip(progresses, speeds)]

    #ceil을 안쓰고 이런식으로도 가능하다....
    #ceil을 안쓰는 것이 아주 근소하게 더 빠르다. (아래 첫번째 케이스일 경우 평균 1ms)
    progresses = list(map(lambda x: x - 100, progresses))
    progresses = [-(p // s) for p, s in zip(progresses, speeds)]
    print(f'남은 작업일 수: {progresses}')

    #빗물 트래킹, 주식 방법
    #자신 이후에 낮은 것들을 같이 빼버린다.
    for cur in progresses:
        while stack and cur > stack[0]:
            answer.append(len(stack))
            stack = []
        stack.append(cur)
    answer.append(len(stack))
    print(time.time() - start)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
#print(solution([0,3,3,3,3],[1,2,2,1,2,2]))