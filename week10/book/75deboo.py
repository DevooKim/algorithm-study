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
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        result = []
        for i in range(k, len(nums)+1):
            result.append(max(nums[start: i]))
            start += 1
        return result

a = Solution()
print(a.maxSlidingWindow( [1,3,-1,-3,5,3,6,7], 3))