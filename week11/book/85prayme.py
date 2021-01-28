import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
import numpy as np
from typing import List

class Solution:
    def fib(self, n: int) -> int:
        # F0 = 0, F1 = 1, Fn = Fn-1 + Fn-2
        # F4= F3 + F2
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        return self.fib(n-1) + self.fib(n-2)

    def fib_book(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

    dp = collections.defaultdict(int)
    def fib_memoization(self, n: int) -> int:
        if n <= 1:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.fib(n-1) + self.fib(n-2)
        return self.dp[n]

    def fib_tabulation(self, n: int) -> int:
        self.dp[1] = 1

        for i in range(2, n + 1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[i]

    def fib_save_memory(self, n: int) -> int:
        x, y = 0, 1
        for i in range(0, n):
            x, y = y, x + y
        return x

    def fib_matrix(self, n: int) -> int:
        M = np.matrix([[0,1], [1,1]])
        vec = np.array([[0], [1]])

        return np.matmul(M ** n, vec)[0]


    
    


        

print(Solution().fib(0)) # 1
print(Solution().fib(1)) # 1
print(Solution().fib(2)) # 1
print(Solution().fib(3)) # 2
print(Solution().fib(4)) # 3
print(Solution().fib(5)) # 5
print(Solution().fib(6)) # 8
