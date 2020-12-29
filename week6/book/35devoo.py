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
    result = []

    def dfs(elements, start, k):
      if k == 0:
        result.append(elements[:])

      for i in range(start, n + 1):
        elements.append(i)
        dfs(elements, i + 1, k - 1)
        elements.pop(0)
    dfs([], 1, k)
    return result

a = Solution()
print(a.combine(4, 2))