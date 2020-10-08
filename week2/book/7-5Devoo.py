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
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            mul = functools.reduce(lambda x, y: x*y, nums[:i], 1)
            mul = functools.reduce(lambda x, y: x*y, nums[i+1:], mul)

            result.append(mul)

        return result

a = Solution()
print(a.productExceptSelf([-1,-1,1,-1,-1,1]))
