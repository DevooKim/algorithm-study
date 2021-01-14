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
        def bs(arr, offset):
            if len(arr) == 1:
                return -1

            mid = len(arr) // 2
            # print(arr[mid] == target, arr)

            if arr[mid] == target:
                return offset + mid

            if arr[mid] > target:
                return bs(arr[:mid], offset)
            else:
                return bs(arr[mid:], offset + mid)
        if nums[0] == target:
            return 0
        return bs(nums, 0)

a = Solution()
print(a.search([-1,0,3,5,9,12], 9))