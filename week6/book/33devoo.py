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
  def letterCombinations(self, digits: str) -> List[str]:
    phone = {
      2: ['a', 'b', 'c'],
      3: ['d','e', 'f'],
      4: ['g', 'h', 'i'],
      5: ['j', 'k', 'l'],
      6: ['m', 'n', 'o'],
      7: ['p', 'q', 'r', 's'],
      8: ['t', 'u', 'v'],
      9: ['w', 'x', 'y', 'z']
    }

    def dfs(s, num):
      if not num:
        answer.append(s)
        return

      for p in phone[int(num[0])]:
        dfs(s + p, num[1:])

    answer = []
    dfs("", digits)
    return answer


a = Solution()

print(a.letterCombinations("23"))