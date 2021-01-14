import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

#풀었는데 맞는건가
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

    def book(self, nums, target):
        if not nums:
            return -1

        #최솟값 찾기
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums)

            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot

        return -1
        
a = Solution()  
print(a.search([4,5,6,7,0,1,2], 1))