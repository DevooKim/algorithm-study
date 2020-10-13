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
        out = []

        p = 1
        for i in range(0, len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1
        for i in range(len(nums) - 1, 0 - 1, - 1):
            out[i] = out[i] * p
            p = p * nums[i]

        print(out)
        return out




Solution().productExceptSelf([1,2,3,4])