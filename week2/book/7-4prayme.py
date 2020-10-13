import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        nums = set(nums)
        for i in range(len(nums)):
            if i == 0:
                # result.append(math.prod(nums[1:]))
                result.append(functools.reduce((lambda x, y: x * y), nums[1:]))
            elif i == len(nums):
                # result.append(math.prod(nums[:-1]))
                result.append(functools.reduce((lambda x, y: x * y), nums[:-1]))
            else:
                # result.append(math.prod(nums[:i] + nums[i+1:]))
                result.append(functools.reduce((lambda x, y: x * y), nums[:i] + nums[i+1:]))
        print(result)
        return result




Solution().productExceptSelf([1,2,3,4])