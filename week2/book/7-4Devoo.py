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
    def arrayPairSum(self, nums: List[int]) -> int:
        '''
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += min(nums[i], nums[i+1])
        
        return result
        '''
        return sum(sorted(nums)[::2])

a = Solution()
print(a.arrayPairSum([1,4,3,2]))
