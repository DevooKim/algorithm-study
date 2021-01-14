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
    def search(self, nums: List[int], target: int) -> int:
        result = [-1]
        def bs(arr, offset):
            if len(arr) == 1:
                return -1

            mid = len(arr) // 2

            bs(arr[:mid], offset)
            bs(arr[mid:], offset + mid)

            if arr[mid] == target:
                result[0] = (offset + mid)
                return offset + mid

        if nums[0] == target:
            return 0

        bs(nums, 0)
        return result[0]
        
a = Solution()  
print(a.search([4,5,6,7,0,1,2], 1))