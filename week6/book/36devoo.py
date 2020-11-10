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
            
            # for e in elements:
            #     prev.append(e)
            #     dfs(_sum + e, elements)
            #     prev.pop()

            for idx, e in enumerate(elements):
                prev.append(e)
                if idx > 0:
                    dfs(_sum + e, elements[idx:])
                else:
                    dfs(_sum + e, elements[:])
                prev.pop()
                

                
        dfs(0, candidates)
        return result
a = Solution()

print(a.combinationSum([2,3,6,7], 7))
print(a.combinationSum([2,3,5], 8))