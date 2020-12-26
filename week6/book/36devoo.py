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
    def dfs(s, arr):
      if s == target:
        result.append(prev[:])
      if s > target:
        return

      for idx, a in enumerate(arr):
        prev.append(a)
        if idx > 0:
          dfs(s+a, arr[idx:])
        else:
          dfs(s+a, arr)
        prev.pop()

    dfs(0, candidates)
    return result
a = Solution()
print(a.combinationSum([2,3,6,7], 7))
print(a.combinationSum([2,3,5], 8))