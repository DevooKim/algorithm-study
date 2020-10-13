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
    def arrayPairSum(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return min(nums)

        result = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            result += min(nums[i:i + 1])

        print(result)
        return result

    def arrayPairSum(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return nums[0]

        result = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            result += nums[i]

        print(result)
        return result

    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])



Solution().arrayPairSum([1,4,3,2])
