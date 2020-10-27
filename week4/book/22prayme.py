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

        front, back = 0, 1
        while front < len(T) - 1 and back <= len(T) - 1:

            if T[front] < T[back]:
                # print(f'front: {T[front]}, back: {T[back]} back - front: {back - front}')
                result[front] = back - front
                front += 1
                back = front + 1
                continue

            if front != len(T) - 2 and back == len(T) - 1:
                front += 1
                back = front + 1
                continue

            back += 1

        return result


Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
# Solution().twoPointer([73,74,75,71,69,72,76,73])
Solution().twoPointer([55, 38, 53, 81, 61, 93, 97, 32, 43, 78])
