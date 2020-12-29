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
  def subsets(self, nums: List[int]) -> List[List[int]]:
    result = []
    prev = []
    def dfs(elements):
      result.append(prev[:])

      for idx, e in enumerate(elements):
        prev.append(e)
        dfs(elements[idx+1:])
        prev.pop()
  
    dfs(nums)
    return result

a = Solution()
print(a.subsets([1,2,3]))