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

        print(nums)        
        return max(nums)

a = Solution()
print(a.rob([1,2,3,1]))
print(a.rob([2,7,9,3,1, 2, 3])) #[2,7,11,10,12,12,15]