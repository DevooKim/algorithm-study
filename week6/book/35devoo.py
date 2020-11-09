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
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1, n+1)]

        def dfs(a):
            if len(a) == k and a not in answer:
                answer.append(a)
                return
                
            for i in a:
                next = a[:]
                next.remove(i)

                prev.append(i)
                dfs(next)
                prev.pop()

        answer = []
        prev = []
        dfs(arr)
        return answer

a = Solution()
print(a.combine(4,2))