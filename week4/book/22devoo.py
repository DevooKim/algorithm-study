import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *
import time

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        start = time.time()
        result = []
        for i, t in enumerate(T):
            L = T[i:]
            count = 0
            for l in L:
                if t < l:
                    break
                else:
                    count += 1
            if count == len(L):
                count = 0
            result.append(count)
        print(f'my: {time.time() - start}')
        return result

    def stackSolution(self, T: List[int]) -> List[int]:
        start = time.time()
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                print(stack, answer)
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        print(f'book: {time.time() - start}')
        return answer

a = Solution()

#print(a.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
print(a.stackSolution([73, 74, 75, 71, 69, 72, 76, 73]))

#my: 1.4972984790802002
#book: 0.00183868408203125