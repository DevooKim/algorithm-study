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
    def climbStairs(self, n: int) -> int:
        
        a = collections.deque()
        for i in range(n//2):
            a.append(2)
        if n%2 == 1:
            a.append(1)

        answer = len(set(itertools.permutations(a)))
        while True:
            if a[0] == 2:
                a.popleft()
                a.append(1)
                a.append(1)
                answer += len(set(itertools.permutations(a)))
                continue

            return answer

    def my_counter(self, n: int) -> int:
        
        a = {
            2: n//2,
            1: n%2
        }

        answer = 0
        if a[1] == 0:
           answer += 1
           a[2] -= 1
           a[1] += 2

        while a[2] > 0:
            top = a[2] + a[1]
            bottom_max = max(a[2], a[1])
            bottom_min = min(a[2], a[1])
            

            b = 1
            for i in range(bottom_max+1, top+1):
                b *= i
            answer += b // math.factorial(bottom_min)

            a[2] -= 1
            a[1] += 2
        return answer + 1

    def book_recur(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    dp = collections.defaultdict()
    def book_memoization(self, n: int) -> int:
        if n <= 2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]
        
        





print(Solution().my_counter(3)) # 3
print(Solution().my_counter(4)) # 5
# print(Solution().my_counter(13)) # 13

# print(Solution().climbStairs(2)) # 2
# print(Solution().climbStairs(3)) # 3
# print(Solution().climbStairs(4)) # 5
# print(Solution().climbStairs(5)) # 8
# print(Solution().climbStairs(6)) # 13