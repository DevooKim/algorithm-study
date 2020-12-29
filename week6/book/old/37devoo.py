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
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev = []

        def dfs(elements):
            if len(prev[:]) > len(nums):
                return
            result.append(prev[:])

            for idx, e in enumerate(elements):
                prev.append(e)
                dfs(elements[idx+1:])
                prev.pop()

        dfs(nums)
        return result

    def book(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index, path):
            result.append(path)

            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])
        dfs(0, [])
        return result
                

a = Solution()
print(a.subsets([1,2,3]))