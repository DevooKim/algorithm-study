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
    def climbStairs(self, n: int) -> int:
        a, b = 0, 0 #1계단, 2계단
        result = 0

        if n % 2 == 0:
            b = n//2
        else:
            a, b = 1, (n-1) // 2

        # a += 2
        # b -= 1

        while b:
            l = math.factorial(a + b)
            result += l / (math.factorial(a) * math.factorial(b))
            a += 2
            b -= 1
        return int(result)


a = Solution()
print(a.climbStairs(4))