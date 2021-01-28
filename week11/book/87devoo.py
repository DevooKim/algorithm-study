import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

#내풀이 36ms, 14.1MB
#책풀이 20ms, 14.4MB
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 0 #1계단, 2계단
        result = 0

        if n % 2 == 0:
            b = n//2
        else:
            a, b = 1, (n-1) // 2

        while b:
            l = math.factorial(a + b)
            result += l / (math.factorial(a) * math.factorial(b))
            a += 2
            b -= 1
        return int(result) + 1

    dp = collections.defaultdict(int)
    def book(self, n):
        if n <= 2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.book(n-1) + self.book(n-2)
        return self.dp[n]



a = Solution()
print(a.climbStairs(4))