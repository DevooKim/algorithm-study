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



Solution().arrayPairSum([1,4,3,2])
