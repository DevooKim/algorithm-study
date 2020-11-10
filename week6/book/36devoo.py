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
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        prev = []
        def dfs(_sum, elements):
            if _sum == target:
                result.append(prev[:])
                return
            elif _sum > target:
                return
            
            for e in elements:
                next = elements[:]
                prev.append(e)
                dfs(_sum + e, next)
                prev.pop()
                
        dfs(0, candidates)
        return result
a = Solution()

print(a.combinationSum([2,3,6,7], 7))