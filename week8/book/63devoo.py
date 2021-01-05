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
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(nums)):
            prev = i - 1
            tmp = nums[i]
            while prev >= 0 and tmp < nums[prev]:
                nums[prev + 1] = nums[prev] 
                prev -= 1
            nums[prev + 1] = tmp

a = Solution()
print(a.sortColors([2,0,2,1,1,0]))