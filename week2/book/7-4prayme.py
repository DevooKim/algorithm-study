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
        print(f"nums: {nums}")
        result = []
        for i in range(len(nums)):
            mul = 0
            left, right = 0, len(nums) - 1
            while left < right:
                if left == i:
                    left += 1
                    continue
                elif right == i:
                    right -= 1
                    continue
                mul += nums[left] * nums[right]
                print(f'i: {i} left: {nums[left]} right: {nums[right]} mul: {mul}')
                if left + 1 != right:
                    left += 1
                    right -= 1


            result.append(mul)
        print(result)
        return result




Solution().productExceptSelf([1,2,3,4])