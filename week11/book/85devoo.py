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
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        return self.fib(n-1) + self.fib(n-2)

    #메모이제이션
    dp = collections.defaultdict(int)
    def book(self, n):
        if n <= 1:
            return n
        if self.dp[n]:
            return self.dp[n]
        
        self.dp[n] = self.book(n-1) + self.book(n-2)
        return self.dp[n]

    #타뷸레이션
    dp = collections.defaultdict(int)
    def book2(self, n):
        self.dp[1] = 1

        for i in range(2, n+1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]

        return self.dp[n]

    #메모리 절약
    def book3(self, n):
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x+y
        return x

    #행렬
    def book4(self, n):
        M = np.matrix([[0, 1], [1, 1]])
        vec = np.array([0], [1])
        return np.matmul(M ** n, vec)[0]

        
a = Solution()
print(a.fib(2)) 