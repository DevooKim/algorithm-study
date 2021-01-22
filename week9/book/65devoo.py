import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

#풀었음 내풀이: 240ms/15.5MB, 책풀이: 240ms/23MB
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


    def book(self, nums, target):
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid

            else:
                return -1
        return binary_search(0, len(nums) - 1)

    def book2(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid > target]:
                right = mid - 1
            else:
                return mid
        return -1

    def book3(self, nums, target):
        index = bisect.bisect_left(nums, target)
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

    def book4(self, nums, target):
        try:
            return nums.index(target)
        except ValueError:
            return -1

a = Solution()
print(a.search([-1,0,3,5,9,12], 9))