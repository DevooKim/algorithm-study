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
  def permute(self, nums: List[int]) -> List[List[int]]:
    prev = []
    answer = []
    def dfs(num):
      if not num:
        answer.append(prev)
        return

      for n in num:
        next = num[:]
        next.remove(n)
        prev.append(n)
        dfs(next)

        prev.pop()

    dfs(nums)
    return answer



a = Solution()