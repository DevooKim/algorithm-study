import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        for i, front in enumerate(T):
            for j, back in enumerate(T[i + 1:]):
                if front < back:
                    result[i] = j + 1
                    break
        return result

    def twoPointer(self, T: List[int]) -> List[int]:
        result = [0] * len(T)

        front, back, backback = 0, 1, 2
        while front <= len(T) - 3 and back <= len(T) - 2 and backback <= len(T) - 1:
            print(f'front: {T[front]}, back: {T[back]} back - front: {back - front}')
            print(f'front: {front}, back: {back}, backback: {backback}')


            if T[front] < T[back]:
                result[front] = back - front
                front += 1
                back = front + 1
                backback = back + 1
                continue
            elif T[front] < T[backback]:
                result[front] = backback - front
                front += 1
                back = front + 1
                backback = back + 1
                continue

            if front != len(T) - 3 and back == len(T) - 2 and backback == len(T) - 1:
                front += 1
                back = front + 1
                backback = back + 1
                continue


            back += 2
            backback += 2


        print(result)
        return result

    def book(self, T: List[int]) -> List[int]:
        # 인덱스를 보관하자
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer


Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
# Solution().twoPointer([73,74,75,71,69,72,76,73])
# Solution().twoPointer([55, 38, 53, 81, 61, 93, 97, 32, 43, 78])

