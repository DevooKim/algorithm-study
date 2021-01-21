import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

# 1. 브루트포스: 시간초과
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        result = []
        for i in range(k, len(nums)+1):
            result.append(max(nums[start: i]))
            start += 1
        return result

    def book1(self, nums, k):
        if not nums:
            return nums
        r = []
        for i in range(len(nums) - k + 1):
            r.append(max(nums[i:i + k]))

        return r

    def book2(self, nums, k):
        result = []
        window = collections.deque()
        current_max = float('-inf')
        for i, v in enumerate(nums):
            window.append(v)
            if i < k - 1:
                continue

            if current_max == float('-inf'):
                current_max = max(window)
            elif v > current_max:
                current_max = v
            result.append(current_max)

            if current_max == window.popleft():
                current_max = float('-inf')
        return result

a = Solution()
print(a.maxSlidingWindow( [1,3,-1,-3,5,3,6,7], 3))