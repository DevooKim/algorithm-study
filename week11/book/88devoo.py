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
    def rob(self, nums: List[int]) -> int:
        for i in range(2, len(nums)):
            nums[i] += nums[i-2]

        return max(nums)

    def book(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)

        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp.popitem()[1]

a = Solution()
print(a.rob([1,2,3,1]))
print(a.rob([2,7,9,3,1, 2, 3])) #[2,7,11,10,12,12,15]