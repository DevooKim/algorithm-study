#두 개 뽑아서 더하기
def solution(numbers):
    answer = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    answer = list(set(answer))
    return sorted(answer)


print(solution([2,1,3,4,1]) == [2,3,4,5,6,7])



