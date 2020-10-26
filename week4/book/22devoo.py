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
        for i in range(len(T)):
            count = 1
            L = T[i:]
            while T[i] >= L[count-1] and count < len(L) - 1:
                count += 1
            print(L, count-1)
            result.append(count-1)
        return result

a = Solution()
print(a.dailyTemperatures([55,38,53,81,61,93,97,32,43,78]))