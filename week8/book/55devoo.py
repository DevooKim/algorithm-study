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
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        result = 0

        for _ in range(len(nums) - k + 1):
            result = heapq.heappop(nums)

        return result

a = Solution()

print(a.findKthLargest([3,2,1,5,6,4], 2))