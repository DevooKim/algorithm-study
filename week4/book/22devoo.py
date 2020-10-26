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

a = Solution()
print(a.dailyTemperatures([47,34,47,34,47,47,34,34,47,47,34,47,47,47,47,34,47,34,34,47,34,34,34,47,34,47,34,47,34,47,34,34,34,34,34,47,34,34,47,47,47,47,34,34,47,47,34,47,47,34,47,47,47,34,47,34,34,34,34,47,47,34,34,34,47,47,34,34,34,47,34,34,34,34,47,34,34,34,34,47,47,47,34,47,34,34,47,47,34,47,34,34,47,34,34,34,47,34,34,47,34,47,34,47,47,47,34,47,34,47,47,34,47,47,47,47,47,47,47,34,47,47,47,47,34,34,34,34,47,34,34,34,34,34,47,34,47,47,47,47,34,34,47,47,34,47,34,47,47,47,34,47,34,34,34,47,47,47,34,34,34,34,34,47,47,47,47,34,47,47,34,47,34,34,47,34,47,34,34,34,47,34,34,34,47,47,47,47,47,47,47,47,34,47,47,47,47,34,34,34,47,34,34,34,34,47,47,47,34,34,34,34,47,34,47,34,34,47,47,47,34,34,47,34,47,34,34,47,47,34,34,47,34,47,47,47,47,34,47,34,47,34,47,34,34,34,47,47,47,34,34,47,34,47,34,47,47,34,34,47,34,34,47,34,34,47,47,34,34,47,47,47,34,34,47,47,47,34,47,47,47,47,47,34,34,34,34,34,34,34,47,47,34,47,34,47,47,47,47,47,47,47,47,47,47,34,47,47,47,34,47,34,34,34,47,47,47,47,34,47,34,47,34,47,47,34,34,34,47,34,34,47,34,47,34,47,34,34,34,34,47,47,34,47,47,47,34,47,34,34,47,34,47,34,47,34,47,34,47,34,47,47,34,34,47,34,47,47,47,47,47,34,34,34,47,34,47,34,34,47,47,47,34,47,47,47,47,34,34,47,47,34,34,34,47,47,47,34,47,47,47,34,47,34,34,47,47,34,47,34,34,47,34,34,34,34,47,47,47,34,47,47,34,47,47,34,34,34,34,47,34,34,47,34,47,47,47,34,47,34,34,47,34,47,34,34,34,34,34,34,47,47,47,47,47,47,47,34,34,34,47,34,34,47,47,47,34,47,34,47,34,47,34,47,47,47,34,34,34,34,34,34,34,34,47,47,47,34,47,34,34,34,47,34,47,47,34,47,47,47,34,34,34,34,34,47,34,47,34,34,47,34,47,47,34,34,34,34,47,47,34,34,47,47,34,34,34,34,34,34,34,47,34,34,47,34,34,47,34,34,47,34,34,34,47,47,34,34,47,47,47,34,34,47,47,47,34,47,47,47,47,47,47,47,34,47,47,47,34,47,47,34,47,34,34,47,34,34,34,34,34,34,47,47,47,34,47,47,34,47,34,34,47,34,34,34,47,47,34,47,47,34,34,34,47,47,47,47,34,47,34,34,47,47,47,47,47,34,47,34,34,34,47,47,47,34,34,47,47,34,34,34,34,34,47,34,47,34,47,34,47,47,47,47,47,34,47,34,34,34,34,34,47,34,47,47,34,34,47,34,47,34,47,34,47,34,47,34,47,47,34,47,47,47,47,34,34,47,34,34,34,34,47,34,34,47,34,34,34,34,34,47,34,47,34,47,34,47,47,47,34,47,34,34,47,47,34,34,34,34,34,34,47,47,47,47,47,47,34,34,34,34,34,47,47,34,47,47,34,47,34,34,47,34,34,47,47,47,34,47,34,47,47,47,47,34,47,47,34,34,34,34,34,34,47,47,47,47,47,47,47,47,47,34,34,34,47,34,34,47,34,47,34,47,34,47,34,47,47,47,34,34,34,34,47,34,47,47,47,34,34,34,47,47,34,34,47,47,47,34,47,34,47,47,47,47,34,34,34,34,47,34,47,47,47,34,47,47,34,47,34,47,47,47,34,47,34,47,34,47,47,47,47,47,34,34,34,47,47,47,34,47,34,34,34,34,34,34,34,47,47,47,47,47,47,34,47,47,47,34,34,34,47,47,47,47,47,34,34,47,47,34,34,34,34,47,34,34,34,47,34,47,34,47,47,47,47,47,47,34,47,34,47,34,47,34,34,34,34,34,34,47,47,47,34,34,34,34,34,47,34,34,34,47,47,47,34,47,34,47,34,34,47,47,34,34,47,34,47,47,34,47,34,47,34,47,47,34,34,47,47,34,34,34,47,34,34,47,47,34,47,47,34,34,34,47,34,34,34,47,34,34,34,47,47,34,47,34,47,34,47,34,34,34,47,34,34,47,34,47,34,47,47,47,47,47,47,47,34,47,34,34,47,47,34,34,47,34,34,47,47,47,34,47,34,34,47,47,34,34,34,34,34,47,47,34,47,47,34,47,34,34,34,47,34,34,34,47,47,34,34,34,34,34,47,47,47,34,47,47,47,47,34,47,47,47,47,47,34,34,47,47,47,47,34,34,34,47,34,47,47,34,47,47,34,34,47,47,47,47,47,47,34,47,47,34,34,34,47,47,47,47,34,47,47,47,34,47,47,34,34,34,47,34,34,34,47,34,47,34,47,34,47,47,47,47,34,47,34,47,34,47,34,34,47,34,34,47,34,47,47,47,47,34,47,34,47,34,34,34,34,47,34,34,34,47,34,47,47,34,47,34,47,34,47,47,47,47,47,47,34,34,47,47,34,34,47,47,47,47,47,34,47,34,34,47,47,34,34,47,47,47,34,47,34,47,34,47,47,34,47,34,34,47,34,34,47,47,47,34,34,47,47,34,47,47,47,34,47,34,34,47,34,34,47,47,34,34,47,47,34,34,47,47,34,47,34,34,47,34,34,47,47,47,47,47,34,47,47,34,34,34,34,34,47,47,34,47,47,34,47,47,34,47,47,47,47,34,34,34,34,34,34,34,47,34,47,47,34,34,34,47,34,34,47,34,47,47,34,34,47,47,34,47,47,47,47,47,47,47,47,34,34,47,47,47,34,34,34,47,47,47,47,47,47,34,47,47,47,34,34,34,34,34,34,47,47,34,47,34,47,47,47,34,34,47,34,34,34,34,47,34,34,47,34,47,47,34,34,47,34,34,34,47,34,47,47,34,47,47,34,47,47,34,34,47,47,34,34,34,47,47,47,47,47,34,34,34,34,34,34,47,47,34,34,34,34,34,47,34,47,34,47,47,34,47,47,47,47,34,47,34,47,47,34,34,47,47,34,34,47,47,47,47,34,47,47,47,34,47,47,34,34,47,47,34,34,34,47,47,34,34,47,34,34,34,47,47,34,34,34,47,47,34,47,47,47,47,47,47,34,47,47,47,47,34,34,47,47,47,34,34,47,47,47,34,34,47,47,47,47,34,34,47,47,34,47,47,34,47,47,47,47,47,47,47,47,47,47,47,47,34,34,47,34,47,47,34,34,47,34,34,34,34,34,47,34,47,47,47,34,47,47,34,34,34,47,47,47,47,47,34,47,47,47,34,47,34,34,34,47,34,34,34,47,47,47,47,34,34,34,34,34,47,47,34,47,47,34,47,47,47,34,34,34,34,47,34,47,47,47,47,47,47,47,34,34,47,47,47,34,34,34,34,34,34,34,47,34,47,34,34,47,34,34,34,47,34,34,47,47,34,47,34,47,47,34,34,34,34,47,47,34,34,34,47,47,34,47,47,34,34,47,34,47,34,34,34,47,34,34,34,34,47,47,34,47,47,34,34,47,34,34,34,47,34,34,34,34,34,47,34,47,34,34,34,34,34,34,47,34,34,47,34,47,34,34,34,47,47,47,34,34,47,47,47,34,47,34,47,34,34,34,34,34,34,47,34,34,34,47,34,34,47,34,47,34,47,47,47,34,34,47,34,47,47,47,47,34,47,47,34,34,47,34,34,34,34,34,34,34,47,34,47,47,47,34,34,47,34,34,34,34,34,34,34,34,47,34,47,34,34,47,34,47,47,34,34,47,47,47,47,34,34,34,34,34,47,34,47,34,47,34,47,47,34,34,47,47,47,34,47,34,34,47,34,47,47,47,34,47,34,34,34,34,47,34,34,34,34,47,34,34,47,47,47,34,34,47,47,47,47,47,34,34,34,47,47,47,34,47,47,34,47,34,34,34,34,47,47,47,47,34,47,47,34,34,47,34,47,47,34,47,47,34,34,47,47,47,47,34,47,47,34,34,34,34,47,34,47,47,34,34,47,47,34,47,34,34,47,34,47,34,47,47,47,34,47,34,47,47,47,34,34,47,34,47,34,34,34,47,47,34,47,47,34,34,47,47,47,47,47,34,47,47,47,47,47,47,47,34,47,34,34,34,34,34,34,47,47,34,47,34,47,47,47,34,47,47,34,47,47,47,47,47,34,47,47,47,34,34,34,34,47,47,34,47,47,34,47,34,34,47,34,47,47,34,47,34,34,34,47,47,47,47,34,34,34,34,34,34,34,34,34,34,47,34,47,47,47,34,34,47,47,47,47,47,47,47,34,47,34,47,34,34,34,34,34,47,47,47,47,47,47,34,47,47,34,47,47,34,34,34,47,47,34,34,47,34,34,34,47,47,34,34,47,47,34,34,34,47,34,47,34,47,34,34,47,47,47,47,47,47,34,47,47,47,47,47,47,34,47,34,34,47,34,34,34,34,47,47,47,34,47,34,34,47,47,47,47,34,47,34,34,47,47,34,47,47,34,47,34,47,34,47,47,34,34,34,34,34,47,47,34,47,34,47,34,34,47,34,34,47,34,34,47,47,47,47,34,47,34,47,47,47,34,34,47,34,47,34,34,34,47,47,34,34,34,34,34,34,47,47,47,47,47,47,47,34,47,47,47,34,34,47,34,34,47,47,34,47,47,34,47,47,34,34,34,47,34,47,34,34,47,47,34,47,47,47,34,34,47,34,34,34,47,47,34,34,34,34,34,47,34,47,47,34,34,47,34,47,47,34,47,47,34,47,47,34,47,47,47,34,34,47,47,34,34,34,34,47,47,47,34,34,47,47,34,34,47,47,34,47,34,47,34,34,34,34,34,34,34,34,34,47,47,47,47,34,34,34,47,47,47,47,47,34,47,47,34,47,34,47,47,34,47,34,34,47,34,34,47,47,47,47,47,34,34,34,47,34,47,47,47,47,47,47,34,34,47,34,47,47,34,47,47,34,34,34,47,47,47,34,47,47,47,47,47,34,47,34,47,34,47,34,34,34,47,47,47,34,47,47,47,34,47,47,47,47,47,47,34,47,47,47,47,34,47,34,34,47,47,34,47,34,47,47,34,47,34,34,34,47,47,34,47,34,47,34,47,34,34,47,34,47,47,47,34,47,34,47,47,34,34,47,34,47,34,34,34,34,34,34,47,34,34,34,34,34,34,34,47,47,47,47,47,47,34,47,47,47,34,47,34,47,47,34,34,34,34,34,47,47,47,47,47,47,34,47,47,47,47,34,47,47,47,47,34,34,47,47,47,47,34,47,34,47,47,47,34,47,34,47,34,47,34,47,47,34,47,47,34,34,47,47,34,47,47,47,47,47,34,47,47,47,34,47,47,47,47,47,47,47,47,47,34,34,47,34,34,34,47,47,34,47,47,47,34,34,47,34,47,47,34,34,34,47,47,34,47,47,47,47,47,34,34,34,34,47,47,34,47,34,34,34,34,34,47,47,34,47,47,34,47,34,34,47,34,34,34,47,47,34,34,34,47,34,34,34,47,34,47,34,34,47,47,34,34,34,47,34,34,47,34,47,34,34,47,47,47,47,34,47,34,34,47,34,34,34,47,47,34,47,34,47,47,34,47,47,47,47,47,34,34,47,34,34,47,47,47,47,47,47,47,47,34,47,34,47,47,34,34,34,34,34,47,47,47,47,34,47,34,47,47,34,47,34,47,34,47,34,47,34,34,47,34,47,47,34,47,34,47,47,34,34,47,34,34,47,34,47,47,47,47,34,34,47,34,34,47,34,47,47,47,47,34,47,47,34,34,47,47,47,47,34,47,34,47,34,47,47,34,47,34,47,34,47,47,34,34,47,47,47,47,34,34,34,47,47,47,47,34,34,47,34,47,47,47,34,47,47,34,47,34,47,47,34,34,34,47,34,47,47,34,47,47,34,47,34,34,34,47,47,34,34,47,47,47,34,47,47,34,47,47,47,34,34,47,34,47,47,47,47,34,47,34,34,34,47,47,47,47,34,47,47,47,34,34,47,34,47,34,47,34,47,47,34,34,34,34,34,34,47,47,34,34,34,47,34,47,34,34,34,47,34,47,34,34,34,47,34,34,47,47,47,34,34,34,34,34,34,34,47,34,47,34,34,47,34,47,47,34,47,47,34,47,47,34,47,34,34,34,47,47,34,47,34,47,34,47,47,34,34,47,47,34,34,47,47,34,34,34,47,34,47,47,34,47,34,34,34,47,47,47,34,34,34,34,34,34,47,34,47,34,34,34,47,47,47,34,34,47,34,34,47,47,47,47,34,34,47,47,47,47,47,34,34,34,34,47,34,34,47,47,47,34,47,34,34,34,34,47,34,34,34,47,47,34,34,47,47,47,34,34,47,34,34,47,47,47,47,47,34,34,34,47,47,47,34,47,34,34,34,47,34,34,34,34,47,47,47,34,34,47,47,47,47,34,47,34,47,34,34,34,47,47,47,47,47,47,34,34,47,47,34,34,34,47,34,47,34,34,34,34,34,47,34,47,47,34,47,47,34,34,34,47,34,47,47,47,47,47,34,47,47,34,34,47,34,47,47,34,47,34,34,47,34,47,34,47,34,34,47,47,47,47,47,47,34,34,34,34,47,34,34,47,34,34,47,34,47,47,34,34,47,47,47,34,47,34,34,34,47,47,34,34,47,47,34,47,47,34,34,34,34,34,34,34,47,34,34,47,47,47,34,34,47,47,47,34,34,47,34,34,34,34,34,34,34,34,47,34,34,34,47,47,34,47,34,34,47,34,34,34,47,34,34,47,34,34,34,47,34,34,47,34,47,34,47,34,34,47,34,47,47,34,47,34,34,47,34,47,47,47,34,34,47,47,47,47,34,34,34,34,34,47,47,47,34,47,34,34,34,47,47,34,34,47,34,47,47,47,47,47,47,47,34,34,34,47,34,47,34,47,34,34,47,47,34,47,47,47,47,47,47,47,47,34,34,34,34,47,47,47,47,47,34,34,47,34,34,34,47,34,47,47,34,34,34,34,34,34,34,34,34,47,34,34,47,47,47,34,34,34,47,47,47,47,47,47,47,47,47,47,34,47,47,47,47,34,47,34,34,34,47,47,34,47,47,47,47,34,47,34,34,34,47,47,47,47,34,47,34,47,34,34,47,47,34,34,34,34,47,47,47,47,47,34,47,34,34,34,34,47,47,34,47,34,34,34,47,47,34,34,47,47,47,47,47,34,47,47,47,34,47,47,47,47,47,34,34,47,34,34,34,34,47,47,47,34,47,47,34,47,47,47,34,47,47,47,47,47,34,47,47,47,47,34,47,47,47,47,47,34,47,34,47,47,34,47,34,34,47,47,34,47,47,47,47,47,34,34,47,34,47,47,34,34,47,34,47,47,47,34,34,34,34,34,34,47,34,34,47,34,47,47,47,47,34,34,34,34,47,34,47,34,47,34,34,34,34,34,47,34,34,34,47,47,34,34,47,34,34,47,34,34,47,47,47,34,47,47,47,34,47,34,34,47,47,47,34,47,34,47,34,34,47,47,34,47,34,47,47,34,34,34,47,34,47,47,47,34,47,34,34,34,47,34,47,47,34,47,47,47,34,47,34,47,47,34,34,47,34,34,34,34,47,47,34,34,34,34,34,34,47,34,34,47,34,47,47,47,47,34,34,47,34,47,34,34,34,34,34,47,34,47,47,34,47,47,34,47,34,47,34,34,47,34,47,47,34,34,34,34,34,34,34,47,47,47,34,34,34,34,34,47,34,34,47,47,34,34,34,47,47,34,34,47,47,34,34,47,47,34,47,47,47,47,47,47,47,34,47,34,34,47,34,34,34,34,47,34,47,34,47,34,34,34,34,47,34,47,47,34,34,47,47,34,34,34,34,47,47,47,47,47,47,34,34,47,34,47,47,34,47,34,34,34,47,47,47,47,47,34,34,34,47,47,47,47,34,34,34,34,47,47,47,34,34,34,34,34,47,34,34,47,47,47,47,34,47,34,47,47,47,34,34,47,34,47,47,34,47,47,34,34,47,47,47,47,47,34,34,34,34,47,34,47,47,47,47,47,34,34,47,47,34,47,47,34,34,34,34,47,47,34,47,34,47,34,47,34,34,47,34,47,34,47,47,47,47,47,34,34,34,47,47,34,34,34,47,34,47,34,34,34,34,34,34,34,34,47,34,34,34,47,34,47,47,34,47,34,47,34,47,47,47,34,34,47,34,47,47,34,47,47,34,47,34,47,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,47,47,47,34,34,34,47,47,34,47,34,47,34,34,34,47,34,47,34,47,34,47,47,47,34,47,47,47,34,47,47,47,47,34,47,47,34,34,47,47,47,34,47,47,47,34,47,47,34,34,47,47,47,47,34,47,34,47,34,47,34,34,34,47,47,34,47,34,34,34,34,34,47,34,34,34,47,47,47,47,47,34,47,34,47,34,47,34,47,34,47,34,47,34,47,34,47,34,47,34,34,34,34,47,34,34,47,47,47,47,47,47,34,34,47,47,34,34,34,34,34,34,47,47,47,47,34,47,34,47,47,47,34,34,47,47,34,34,34,34,34,34,47,34,34,47,34,47,34,47,34,34,47,34,34,34,47,34,47,34,34,47,47,34,47,47,47,34,47,34,34,34,47,34,34,34,34,47,47,34,34,34,34,34,47,34,47,34,47,34,47,34,47,34,34,47,34,47,47,34,47,47,47,34,47,34,47,47,47,34,47,47,47,47,34,47,47,47,47,34,47,47,47,34,47,47,47,34,47,34,34,47,47,47,47,47,34,34,34,47,34,34,47,47,34,34,34,47,47,47,34,34,34,34,34,47,34,47,34,34,47,34,47,47,47,34,34,47,34,34,34,34,34,34,47,47,47,34,34,47,34,47,47,47,47,34,47,34,34,34,47,34,47,34,34,47,47,47,47,47,47,47,34,34,47,47,47,47,47,47,47,34,34,34,47,47,47,47,47,34,34,34,34,34,34,47,34,34,47,34,34,47,47,34,47,34,47,34,47,47,47,34,34,34,34,34,34,34,47,34,47,34,47,47,34,34,34,34,47,34,47,47,34,34,47,34,47,34,34,47,47,47,34,47,47,47,34,34,47,34,47,34,47,34,34,47,34,47,47,47,47,47,34,34,47,47,47,47,47,47,34,34,47,47,34,34,34,34,47,47,47,34,34,34,47,34,34,47,47,47,47,47,34,47,34,47,47,34,47,47,34,47,47,34,34,47,47,34,47,34,47,47,34,34,34,47,34,47,34,34,47,47,34,34,34,34,34,34,34,47,34,47,47,47,34,34,47,34,47,47,47,34,34,47,34,47,47,34,34,34,34,47,47,47,34,34,47,34,34,47,47,47,47,47,47,34,47,34,47,47,34,47,34,34,34,34,47,34,47,34,34,34,47,34,47,47,47,47,34,34,47,34,47,34,47,47,47,34,34,34,47,47,34,34,34,34,47,34,47,47,47,34,47,34,34,47,34,47,47,47,47,47,47,47,47,47,34,47,47,34,47,34,47,47,47,47,47,47,47,34,34,47,47,34,34,34,34,34,47,34,34,34,47,47,47,34,34,47,34,47,47,34,34,47,34,34,47,47,47,47,47,34,34,47,47,34,47,34,47,34,34,47,47,34,34,47,47,34,34,47,47,34,47,47,47,47,34,34,34,34,34,34,34,34,47,47,34,34,47,47,47,47,47,34,47,47,34,47,34,47,34,34,34,47,34,34,47,34,34,34,34,34,47,47,47,34,47,34,47,34,34,34,34,47,47,34,47,34,34,47,34,34,34,34,34,34,34,47,47,34,34,47,34,47,34,47,47,34,47,34,47,47,47,34,47,34,47,34,34,47,47,47,47,47,34,34,34,34,47,34,34,47,34,47,34,34,34,34,34,47,47,34,47,47,47,47,47,34,34,34,47,47,34,47,47,47,34,47,47,34,47,34,47,34,34,34,34,34,47,47,34,34,47,34,47,34,34,34,34,34,47,47,47,47,47,47,47,34,47,47,47,47,34,34,34,47,47,34,34,34,47,47,47,34,34,34,47,47,34,34,47,34,34,47,34,47,34,34,34,34,34,34,47,34,47,34,34,34,34,47,47,34,47,34,47,34,47,34,47,47,34,47,47,47,47,34,47,34,34,34,47,47,47,47,47,34,47,34,34,34,34,34,47,34,34,34,47,34,47,47,34,47,34,47,47,47,47,34,34,47,34,34,34,47,34,34,34,34,34,34,47,34,47,47,47,47,47,47,34,47,47,34,34,47,47,34,47,47,47,34,34,34,34,34,47,47,34,47,34,34,34,47,34,34,34,34,47,47,34,47,47,47,34,47,47,47,47,34,34,34,47,34,47,47,47,34,47,47,34,47,34,47,34,34,47,47,47,34,34,47,47,47,34,47,47,34,34,47,47,47,34,34,34,34,47,47,47,34,47,47,34,34,47,47,47,47,34,34,34,47,47,34,34,34,47,47,34,47,34,34,47,47,47,34,34,34,34,34,34,34,34,34,34,34,34,34,34,47,34,47,34,47,34,47,34,47,47,47,34,47,34,47,34,47,34,34,34,47,47,34,47,34,34,47,47,47,34,47,34,47,47,47,34,34,47,34,34,34,34,47,47,47,47,34,47,34,47,47,47,47,34,34,47,47,34,47,34,47,47,34,47,34,34,34,47,34,34,47,47,47,47,47,47,34,34,34,34,47,34,47,47,47,47,47,34,34,34,47,34,47,34,47,47,34,34,47,47,34,47,34,47,34,34,34,34,47,34,34,34,47,34,34,34,47,34,34,34,47,47,47,47,47,34,34,34,34,47,34,34,47,47,47,34,34,47,34,34,47,47,34,34,47,47,47,47,47,34,47,47,34,47,34,47,34,47,47,47,34,34,34,34,47,34,34,47,34,47,47,47,47,34,47,34,47,34,34,34,47,47,34,34,47,47,47,34,34,47,34,47,34,47,34,47,34,47,47,47,34,34,47,47,47,47,34,47,47,47,47,34,47,47,47,34,34,34,47,47,34,47,47,34,34,47,34,34,47,47,47,47,47,47,47,47,47,34,34,34,47,47,34,34,47,47,47,47,47,47,47,47,47,34,34,34,47,34,34,34,47,34,47,47,47,47,47,34,34,34,34,34,34,34,34,47,47,47,47,34,47,34,47,47,47,34,47,34,34,34,47,47,47,47,34,47,47,34,47,47,34,34,34,47,34,34,34,47,34,34,34,34,47,47,47,47,34,34,47,47,47,47,34,47,47,34,34,34,47,47,34,34,34,47,47,47,34,47,47,34,47,34,47,47,47,34,34,47,34,34,34,34,47,47,47,47,34,34,47,34,47,47,47,47,34,47,34,34,47,47,47,34,47,34,34,47,34,34,47,34,34,47,34,47,34,47,34,34,47,47,47,34,47,47,34,47,34,47,34,47,34,34,34,47,47,47,47,47,47,47,34,47,34,34,34,47,34,47,47,34,47,34,47,34,34,47,34,47,34,47,34,47,34,47,47,34,34,34,47,47,34,47,47,47,47,34,34,47,47,34,34,34,34,34,47,34,47,34,34,47,47,34,47,47,34,34,47,34,34,34,34,47,47,34,34,47,34,47,34,47,34,34,34,34,34,47,34,47,47,47,47,47,47,47,34,47,34,47,47,47,34,34,34,34,47,34,47,47,34,47,34,34,34,47,34,34,47,34,47,47,47,47,34,34,34,47,34,34,34,47,47,34,47,34,34,47,34,47,34,34,47,34,34,34,47,34,47,34,47,34,47,47,34,47,47,34,47,47,34,47,34,47,34,34,34,34,47,47,47,34,34,34,47,47,47,47,34,34,34,47,47,34,34,34,34,34,34,34,34,47,34,47,47,47,47,47,34,34,34,34,47,47,47,34,47,47,47,47,47,47,47,34,34,47,34,47,34,47,47,34,47,34,47,47,47,47,34,34,34,34,47,34,34,34,34,34,47,47,34,47,34,47,34,34,34,47,34,34,47,47,34,47,47,34,47,47,34,34,34,47,34,34,47,47,47,34,34,34,47,34,34,47,47,47,34,34,34,34,47,34,47,34,47,34,47,47,34,47,34,34,34,34,47,47,47,47,47,34,47,47,47,47,34,34,34,47,47,47,34,47,47,34,47,47,34,47,47,47,34,34,47,34,47,34,47,34,47,47,34,47,34,47,47,34,34,34,34,34,47,47,47,47,47,34,47,47,34,34,47,47,34,34,34,47,47,47,34,47,34,34,47,34,47,47,47,47,47,34,47,34,47,34,47,34,47,34,34,34,47,34,47,34,47,34,34,47,47,47,34,34,34,47,34,34,34,47,47,47,47,34,47,47,34,34,47,34,34,34,47,34,34,47,34,34,47,47,47,47,34,34,34,34,47,47,34,47,34,47,34,34,34,47,47,34,34,47,34,47,47,34,34,47,34,34,34,34,34,47,34,47,47,47,34,47,47,47,34,47,47,47,47,34,47,34,47,47,47,34,34,34,47,47,34,34,34,47,47,34,47,34,34,34,47,34,34,47,34,47,47,47,47,34,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,34,34,47,47,34,47,34,34,34,34,34,34,47,47,47,47,34,34,47,47,47,47,34,34,34,34,34,47,47,47,47,47,34,47,34,47,47,34,34,47,34,34,47,47,47,34,47,34,47,34,34,47,47,34,47,34,47,47,47,47,47,47,34,34,47,47,47,34,47,34,34,34,34,47,47,34,34,47,34,34,34,34,47,34,34,47,34,47,34,34,47,34,34,47,47,34,34,47,47,47,47,47,34,34,34,34,47,34,47,34,34,47,34,34,34,34,47,47,47,47,47,47,34,34,34,47,34,34,47,34,47,47,34,47,34,47,47,47,47,34,47,34,47,47,34,47,34,34,47,34,34,34,47,34,47,34,47,47,34,34,47,34,47,47,47,47,34,34,34,47,47,34,47,34,34,47,47,47,47,34,34,47,34,34,34,47,47,47,34,47,47,47,34,34,34,34,34,34,47,47,47,34,47,47,47,34,34,34,47,34,34,34,47,47,34,34,47,47,47,47,47,47,47,34,34,47,34,34,47,34,34,47,47,34,47,47,47,47,34,34,47,34,47,47,34,34,47,34,47,34,34,34,34,47,34,47,34,47,47,47,34,47,34,34,34,47,47,34,47,47,47,34,34,47,47,34,47,34,47,47,34,47,34,47,34,34,34,47,47,34,47,47,34,34,47,34,47,47,47,47,34,34,47,47,34,47,47,34,47,34,34,34,47,47,34,47,34,34,34,47,47,34,34,34,34,34,34,34,34,47,47,47,34,34,34,34,47,47,47,34,47,47,34,34,47,34,34,34,47,34,47,34,47,47,47,34,34,47,47,47,34,47,47,47,34,34,47,34,47,47,47,47,34,34,34,47,34,34,47,47,34,34,47,34,47,34,34,34,34,47,47,34,34,34,34,34,34,47,34,47,47,47,34,47,34,47,47,34,34,34,34,47,34,34,47,47,34,34,47,34,47,34,47,47,34,47,47,47,34,47,34,47,34,47,34,34,47,47,34,34,34,34,47,34,47,47,34,47,34,47,34,34,34,47,47,47,34,47,34,34,47,47,34,47,47,47,47,47,47,47,47,34,47,34,47,34,34,34,34,47,47,34,47,47,47,47,47,47,47,47,34,34,34,34,34,47,47,34,47,47,47,47,34,34,47,47,34,34,34,34,47,34,34,34,47,47,34,34,34,47,34,34,47,47,34,34,47,34,47,47,47,47,47,34,34,47,47,47,47,47,47,34,47,47,47,34,47,47,34,34,47,47,34,34,34,34,47,47,34,47,47,34,34,34,47,47,47,34,47,47,34,34,47,34,47,47,34,34,47,47,47,47,47,47,47,34,34,34,34,34,34,34,34,47,34,47,47,34,47,34,47,47,47,34,34,34,47,34,47,34,34,47,34,47,34,47,34,47,34,34,47,47,34,47,47,47,34,47,47,47,47,47,47,34,47,34,34,47,34,34,34,34,47,47,34,47,34,34,34,34,47,34,34,47,34,34,34,47,34,47,47,34,34,34,47,47,47,34,34,34,34,34,47,47,34,47,47,34,47,47,34,34,34,34,34,34,34,34,47,34,47,47,47,34,34,34,47,47,47,34,47,47,47,47,47,47,47,34,34,47,47,34,34,34,34,34,34,47,47,34,34,34,47,34,47,34,34,34,47,47,47,47,47,47,34,34,47,34,47,34,47,34,34,47,34,47,34,34,47,47,47,47,34,34,47,34,47,47,47,47,34,34,47,34,34,34,34,47,47,34,34,47,47,47,47,34,47,34,47,47,34,34,34,34,47,34,34,34,47,34,34,47,47,34,34,47,34,34,34,47,47,34,47,34,47,47,34,47,34,34,34,34,47,47,47,34,47,47,34,47,34,34,34,47,34,34,34,34,34,47,47,47,47,47,34,47,34,47,47,47,47,34,34,34,47,47,34,34,34,47,47,47,34,34,34,47,34,34,47,47,47,47,34,34,47,47,34,47,47,47,47,34,47,34,34,34,47,47,47,34,47,47,47,47,34,47,47,47,34,34,34,47,34,34,34,47,34,34,47,34,47,47,34,47,47,34,34,34,47,34,47,47,34,34,34,47,34,47,47,34,34,47,47,34,47,34,47,47,47,47,47,34,47,34,34,47,47,34,34,47,47,47,47,34,47,34,34,34,47,34,47,34,47,34,47,47,47,34,34,34,47,47,34,47,34,34,47,47,47,47,34,47,47,47,34,47,47,47,47,47,34,34,47,34,34,47,34,47,34,34,47,47,34,34,47,47,34,34,34,47,47,47,34,34,34,34,34,47,34,47,34,47,47,47,34,47,47,47,34,47,34,34,47,34,34,47,34,47,47,34,47,47,47,47,34,34,47,34,34,47,34,34,34,34,47,47,47,34,47,34,47,47,47,34,34,34,47,34,47,47,47,47,47,47,47,47,34,47,47,47,34,34,47,47,47,34,34,47,34,34,47,47,34,47,34,34,47,47,47,34,47,47,47,47,34,34,47,34,34,34,34,47,34,47,34,47,34,34,34,34,47,34,34,47,34,34,34,47,34,47,47,34,47,34,34,34,34,47,47,47,47,47,47,47,47,47,47,34,34,47,47,47,34,47,47,34,34,34,47,34,34,47,34,34,34,34,34,47,47,47,34,47,47,34,34,34,34,34,47,34,47,47,34,34,34,47,34,34,47,47,47,47,34,34,34,34,47,47,47,34,47,34,34,34,47,47,34,34,47,34,47,47,34,47,47,34,34,34,34,47,34,34,34,34,47,47,34,34,34,34,34,34,34,34,34,34,34,34,34,47,34,47,34,34,34,47,47,47,34,47,34,47,47,47,47,34,34,47,47,47,34,47,34,34,34,47,34,47,47,47,34,47,47,34,47,47,34,47,34,34,47,34,34,47,47,47,34,34,47,34,47,34,47,47,47,34,47,47,34,47,47,34,47,47,47,34,34,47,47,34,34,47,47,34,47,34,47,34,34,34,34,47,34,47,47,47,47,47,34,47,47,34,34,47,34,34,47,47,47,47,47,47,34,47,34,34,47,34,34,34,47,47,34,47,47,47,47,47,34,47,34,47,47,34,34,34,47,34,34,47,34,34,47,34,34,34,47,34,34,34,34,47,34,47,34,47,47,47,47,47,34,34,34,47,47,34,34,34,47,34,34,34,47,34,34,34,34,34,47,34,34,34,47,47,47,34,47,34,47,34,34,47,47,34,34,34,47,34,47,47,47,47,47,34,47,47,34,47,47,34,47,47,47,34,47,47,47,47,47,34,47,34,34,34,47,34,34,47,34,47,34,47,34,47,47,34,47,47,47,34,34,34,34,34,34,34,47,34,34,34,34,34,47,47,47,34,34,47,34,34,47,34,34,47,47,47,34,34,47,47,47,47,34,47,47,47,34,34,47,47,34,34,47,47,34,34,47,47,47,47,47,34,34,47,47,34,47,47,47,34,34,34,47,34,47,34,47,34,34,34,47,34,47,47,47,34,34,34,47,34,47,47,34,34,34,47,34,34,47,47,34,47,47,47,47,34,47,47,34,34,34,47,34,47,34,47,47,47,34,34,47,34,47,47,47,47,34,47,47,47,47,34,34,34,34,47,47,47,47,34,47,34,47,34,34,34,47,47,34,47,34,34,34,34,34,34,34,47,47,47,47,47,34,34,34,47,34,34,34,34,34,34,34,34,34,47,34,34,34,47,34,34,47,47,34,34,47,34,47,34,47,47,47,34,47,47,47,34,47,34,47,47,47,34,34,34,34,47,34,34,34,34,34,34,47,47,34,34,47,34,47,47,34,34,34,47,47,47,47,34,34,47,47,34,34,34,34,34,34,34,34,47,34,47,47,34,47,34,47,47,47,47,34,47,47,47,34,47,34,34,47,47,34,34,47,47,34,34,34,34,47,47,34,47,34,47,47,47,34,34,34,47,47,34,34,34,47,47,47,47,47,47,47,47,34,47,34,47,47,47,34,34,47,34,34,47,34,34,34,47,47,47,34,34,34,47,34,47,34,47,47,34,47,47,47,34,34,34,47,34,34,47,34,47,34,34,34,34,34,34,47,47,34,34,34,34,34,34,47,47,47,47,34,47,47,34,47,47,47,47,34,34,34,34,34,34,47,34,34,47,47,34,47,47,34,47,47,47,34,34,34,34,47,47,34,34,47,47,47,34,34,47,47,34,34,47,47,34,47,34,47,47,47,47,34,47,47,34,47,34,34,47,47,47,47,47,34,34,47,47,47,34,34,47,34,47,47,47,34,34,47,47,47,34,47,47,47,34,34,47,47,47,47,47,34,47,47,34,47,34,34,34,47,34,34,47,34,47,47,47,34,34,47,47,47,34,47,34,47,34,47,47,47,34,47,34,47,47,34,47,47,34,47,47,47,34,47,34,47,47,47,47,47,47,47,34,47,47,47,47,47,34,34,34,47,34,47,34,47,34,34,34,47,47,34,47,47,47,47,34,34,34,34,34,34,47,34,34,34,47,47,34,34,34,34,47,47,47,47,34,34,47,47,34,47,47,34,34,47,47,34,47,34,47,47,47,47,47,34,34,34,34,34,47,47,34,34,34,34,47,34,47,34,34,47,47,47,34,34,34,34,47,47,34,47,34,34,34,34,34,47,47,34,47,34,47,47,47,34,47,34,47,47,34,47,47,34,34,47,47,34,34,47,34,34,34,34,34,34,47,47,34,34,34,34,34,47,47,34,47,47,47,47,47,34,34,34,47,47,34,47,34,47,47,34,34,47,34,34,34,47,34,47,34,47,34,34,47,34,47,47,34,47,34,47,34,34,34,47,34,47,47,34,47,34,34,34,34,34,47,34,34,47,34,34,34,47,47,34,47,34,34,47,47,47,47,47,47,34,34,47,47,47,34,47,47,47,34,47,47,47,34,34,47,34,47,34,47,34,47,47,34,34,47,47,47,47,47,34,47,34,47,34,47,47,47,47,47,34,47,47,47,34,47,47,47,34,34,47,34,34,47,47,34,34,47,34,34,34,34,34,34,34,34,47,47,47,47,47,34,34,47,47,34,34,47,34,47,34,47,34,34,34,34,34,34,34,47,47,47,34,47,34,47,34,34,34,34,47,47,34,34,34,47,34,47,34,34,47,34,34,47,47,34,34,47,34,34,34,34,34,34,47,47,47,34,47,47,34,47,47,34,47,47,47,47,34,47,47,34,34,47,34,34,34,47,47,34,34,34,34,34,34,47,34,47,47,47,34,47,47,34,47,47,47,47,34,47,47,34,47,47,47,47,34,47,34,34,34,34,47,47,34,47,34,47,34,34,47,47,47,34,47,47,34,34,47,47,34,34,47,47,34,47,47,47,34,34,34,34,34,47,34,47,47,34,47,34,47,47,34,34,47,34,47,34,47,47,47,34,34,47,47,47,47,34,47,47,47,34,34,47,34,34,34,34,47,34,34,34,47,34,34,47,34,34,34,47,47,34,34,34,34,34,34,34,34,34,34,47,47,47,34,47,34,47,47,34,47,34,47,34,34,47,47,34,47,34,47,34,34,47,34,47,34,34,34,34,34,34,47,47,47,47,47,47,47,34,47,34,34,34,47,34,34,34,34,34,47,34,47,34,34,47,34,34,47,47,47,34,34,47,34,47,34,34,34,34,34,47,47,34,47,47,34,34,34,47,47,47,47,47,34,34,34,34,47,47,47,34,47,34,47,34,34,34,34,34,34,47,47,47,34,34,34,34,47,47,47,34,47,34,34,34,47,47,47,47,34,34,34,34,47,34,47,47,34,47,34,47,34,47,34,34,47,47,34,47,34,47,47,47,47,34,34,34,47,34,47,34,47,34,47,47,47,34,47,47,34,47,47,34,34,47,34,47,34,47,47,47,34,47,47,47,47,34,47,34,34,47,47,34,47,34,47,47,47,47,34,34,47,34,34,47,47,47,34,34,47,34,34,34,34,34,34,47,47,34,34,47,47,47,47,47,34,34,34,34,34,34,47,34,47,47,47,47,47,34,34,34,34,34,34,34,34,47,34,34,34,47,47,34,34,47,34,34,34,47,34,47,47,34,34,47,34,34,47,34,47,47,47,34,47,47,47,47,34,34,34,47,34,47,34,47,34,47,34,34,34,47,34,34,47,34,47,47,34,34,47,47,47,34,47,47,34,34,47,34,34,47,34,47,47,34,34,47,34,47,34,47,34,34,34,34,47,34,34,34,34,34,34,34,47,34,34,47,47,47,47,47,47,34,47,47,34,47,47,47,47,34,34,47,47,47,34,34,47,34,47,47,34,34,34,47,47,34,47,34,47,34,34,34,34,34,34,34,47,47,47,47,34,47,47,34,34,47,47,47,34,34,47,34,47,47,47,47,34,47,34,34,34,47,47,34,34,34,47,34,34,34,34,47,47,34,34,47,47,47,34,47,34,34,34,47,34,34,34,34,34,34,34,34,34,34,34,47,47,47,47,34,47,47,34,47,34,47,47,34,47,34,47,34,47,34,34,34,34,34,34,34,47,34,34,34,47,34,34,34,47,47,47,47,34,34,34,34,47,34,34,47,34,34,47,34,34,47,47,47,34,34,34,47,47,34,34,34,47,34,34,47,34,34,47,34,47,47,47,34,34,34,47,34,47,34,47,47,47,47,34,47,34,34,34,47,47,34,47,34,47,34,34,47,47,47,47,34,47,34,47,34,47,47,34,47,34,47,34,47,47,47,47,34,47,47,47,34,47,34,34,47,34,47,47,47,47,34,34,34,47,34,34,47,47,47,47,34,47,34,47,34,34,47,34,34,47,34,34,47,34,34,47,47,47,47,47,47,34,47,47,47,47,47,47,34,34,34,34,47,34,34,34,34,34,34,34,34,47,34,34,47,34,34,47,47,47,34,47,34,47,47,47,34,34,34,34,47,47,47,47,34,47,47,47,47,34,47,47,34,47,34,34,47,47,47,34,47,34,47,47,47,34,47,47,34,34,34,34,47,47,47,34,34,47,47,47,34,47,34,47,47,47,47,47,34,34,47,34,34,34,34,47,34,34,34,34,34,47,47,47,34,34,34,34,47,47,34,34,47,47,47,34,34,34,47,47,47,34,47,47,34,34,34,47,47,47,47,47,47,34,34,47,47,47,47,34,47,34,34,34,47,47,47,47,34,34,34,34,47,34,47,47,47,47,34,47,47,34,34,47,34,34,47,47,34,34,47,34,47,34,34,34,34,34,34,47,47,47,47,47,34,47,47,34,34,34,34,34,47,47,34,47,47,34,47,47,34,47,34,47,47,47,47,47,47,34,47,34,34,34,34,47,47,34,47,34,34,47,34,34,47,47,47,34,34,34,47,34,34,47,47,34,34,34,47,34,34,34,34,34,34,34,34,34,47,47,34,47,34,34,34,34,34,34,47,47,47,47,47,47,47,34,34,34,47,47,34,34,47,34,47,34,34,47,47,47,47,47,34,47,34,34,34,34,34,34,47,47,47,47,47,34,47,34,34,34,47,34,47,34,47,34,34,47,47,34,34,47,34,47,34,34,47,34,47,47,47,34,34,47,47,34,34,34,34,34,34,47,34,34,47,47,47,47,34,34,34,47,34,34,47,34,34,34,47,34,34,34,47,34,34,34,47,34,47,47,34,47,34,47,47,47,34,47,47,34,47,47,34,34,47,47,34,47,34,47,34,34,34,34,47,47,34,34,34,47,34,34,47,47,34,34,34,34,34,47,47,47,34,47,47,34,34,47,34,34,47,34,34,34,34,34,47,47,34,34,47,34,34,47,34,34,34,47,34,34,47,34,34,47,34,47,47,34,47,34,47,34,47,47,34,34,47,47,47,47,47,34,47,47,34,47,34,47,47,34,34,34,34,47,47,34,47,47,34,47,34,47,47,47,47,47,34,34,34,34,34,47,34,47,34,34,47,34,34,34,47,47,47,47,34,47,47,34,47,47,47,34,47,47,47,34,34,47,34,47,34,34,34,34,34,47,34,47,47,47,34,47,47,47,34,47,47,34,47,47,47,47,34,34,34,47,47,47,34,47,47,34,47,34,34,34,47,47,47,34,34,34,47,47,34,34,34,47,34,34,34,47,47,34,47,34,34,47,47,34,47,47,47,34,47,34,34,47,34,34,34,47,34,34,34,34,34,34,47,34,34,34,47,47,47,34,47,47,34,47,47,34,47,34,47,47,47,34,34,34,34,47,34,34,47,47,34,34,47,47,47,47,47,34,47,34,47,47,34,34,47,34,47,47,34,34,34,47,34,47,34,34,47,34,47,47,34,34,34,47,47,47,47,34,47,47,47,34,34,47,34,34,47,47,47,47,47,34,34,34,34,34,47,34,47,34,34,34,34,34,47,34,47,34,47,47,47,34,47,47,34,34,47,34,47,34,34,34,34,34,47,34,47,47,47,34,47,34,34,34,34,34,34,47,47,34,34,34,47,47,34,34,34,47,47,47,47,34,34,34,47,47,34,47,34,34,47,47,34,47,34,47,34,47,47,47,34,47,47,47,47,34,47,47,47,34,47,47,34,34,47,34,34,47,47,47,47,47,47,47,34,34,34,47,34,47,34,47,47,47,47,34,34,47,34,34,47,47,47,34,34,47,47,47,47,47,34,47,47,47,47,47,47,34,34,47,34,34,34,47,47,47,34,34,47,34,47,47,47,47,34,47,34,47,34,34,34,47,47,47,47,34,34,34,34,47,47,47,47,47,47,47,34,34,47,34,34,34,47,47,34,47,47,47,34,47,34,34,47,47,34,47,34,34,34,47,47,47,47,34,34,34,47,47,47,47,34,34,47,34,47,47,34,34,47,47,34,34,34,34,47,34,34,34,34,47,47,34,34,47,47,47,34,34,47,47,34,34,47,47,34,34,34,47,34,34,47,47,47,47,34,47,34,34,34,34,47,34,47,34,34,47,47,47,34,47,47,34,47,34,47,34,47,47,47,34,47,47,47,47,34,34,34,34,34,34,47,34,47,47,47,47,47,34,47,47,47,34,47,34,47,47,47,34,47,34,47,47,34,47,47,34,34,47,34,47,47,34,34,34,47,47,34,34,34,34,47,34,47,47,47,34,47,34,34,34,34,47,47,34,47,47,47,34,34,47,47,47,34,47,34,47,34,47,34,34,34,47,34,47,34,34,47,34,34,34,47,34,34,47,34,47,47,34,47,34,34,47,34,34,47,47,34,47,34,47,47,47,47,47,47,34,47,34,47,34,47,34,34,34,34,47,34,34,47,34,34,47,34,34,47,47,34,47,34,34,47,47,34,34,34,34,47,47,47,47,34,47,34,34,47,34,34,47,47,34,47,34,34,47,34,47,47,34,47,47,34,47,47,34,34,47,47,34,34,47,47,34,47,34,47,34,34,34,34,47,47,47,34,47,47,34,34,47,34,47,47,47,47,34,47,34,34,34,47,47,47,34,47,34,34,47,34,47,34,34,47,34,47,47,34,47,34,34,47,34,34,34,47,47,34,34,47,47,34,34,47,34,47,34,34,47,34,34,47,47,47,34,34,34,34,34,47,34,34,34,34,47,47,34,34,34,34,34,47,47,47,34,47,34,47,34,47,34,34,47,34,47,47,34,34,47,34,34,34,34,34,34,34,34,34,34,47,47,34,47,34,34,34,34,34,47,34,34,47,34,34,47,34,34,47,47,34,47,47,34,34,34,34,34,34,34,34,34,34,34,34,47,34,47,47,47,34,47,34,34,47,34,34,34,34,34,34,47,47,47,34,47,47,34,34,34,47,34,34,34,47,47,47,34,47,47,34,34,34,47,34,34,34,34,47,34,47,47,34,47,34,34,47,47,47,47,47,34,34,34,34,34,47,47,47,34,47,34,34,47,34,47,47,34,34,34,47,47,34,47,47,34,47,47,47,47,47,47,47,34,34,47,34,34,34,47,47,34,47,47]))