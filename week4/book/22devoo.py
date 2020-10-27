import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
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
        return result

    def stackSolution(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer

a = Solution()
print(a.dailyTemperatures([55,38,53,81,61,93,97,32,43,78]))