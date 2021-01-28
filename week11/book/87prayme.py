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

print(Solution().climbStairs(2)) # 2
print(Solution().climbStairs(3)) # 3
print(Solution().climbStairs(4)) # 5
print(Solution().climbStairs(5)) # 8
print(Solution().climbStairs(6)) # 8
print(Solution().climbStairs(35)) # 5