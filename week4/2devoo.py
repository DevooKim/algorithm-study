import math

def solution(progresses, speeds):
    answer, stack = [], []
    progresses = list(map(lambda x: 100 - x, progresses))
    progresses = [math.ceil(p / s) for p, s in zip(progresses, speeds)]

    #빗물 트래킹, 주식 방법
    #자신 이후에 낮은 것들을 같이 빼버린다.

    for cur in progresses:
        while stack and cur > stack[-1]:
            answer.append(len(stack))
            stack = []
        stack.append(cur)
    answer.append(len(stack))

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))