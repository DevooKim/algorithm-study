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
    def fib(self, n: int) -> int:
        # F0 = 0, F1 = 1, Fn = Fn-1 + Fn-2
        # F4= F3 + F2
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        return self.fib(n-1) + self.fib(n-2)


        

print(Solution().fib(0)) # 1
print(Solution().fib(1)) # 1
print(Solution().fib(2)) # 1
print(Solution().fib(3)) # 2
print(Solution().fib(4)) # 3
print(Solution().fib(5)) # 5
print(Solution().fib(6)) # 8
