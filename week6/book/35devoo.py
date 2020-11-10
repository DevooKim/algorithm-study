import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

#시간초과
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1, n+1)]

        def dfs(a):
            if len(a) == k:
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

    def book(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def dfs(elements, start: int, k: int):
            if k == 0:
                result.append(elements[:])
            
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return result

    def book2(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n+1), k))
    

a = Solution()
print(a.book(4,2))
#print(a.combine(4,2))