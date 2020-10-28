import collections


def solution(progresses, speeds):
    days, prog_deq, spee_deq = 1, collections.deque(progresses), collections.deque(speeds)
    answer = []

    while prog_deq:
        print(f'prog_deq[0]: {prog_deq[0]} spee_deq[0]: {spee_deq[0]}, days:{days}')
        if prog_deq[0] + (days * spee_deq[0]) >= 100:
            complete = 0
            while prog_deq and prog_deq[0] + (days * spee_deq[0]) >= 100:
                prog_deq.popleft()
                spee_deq.popleft()
                complete += 1
            answer.append(complete)

        days += 1

solution([93, 30, 55], [1, 30, 5])