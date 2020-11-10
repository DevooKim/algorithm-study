import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

#풀었음
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
            #result = [[2, 2, 3], [2, 3, 2], [3, 2, 2], [7]]

            for idx, e in enumerate(elements):
                prev.append(e)
                if idx > 0:
                    dfs(_sum + e, elements[idx:])
                else:
                    dfs(_sum + e, elements[:])
                prev.pop()
                
        dfs(0, candidates)
        return result

    def book(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result

    
a = Solution()

print(a.combinationSum([2,3,6,7], 7))
print(a.combinationSum([2,3,5], 8))