import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *

#투포인터로 풀었음
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0, len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -=1
            else:
                return [left+1, right+1]

    def book1(self, numbers, target):
        for k, v in enumerate(numbers):
            left, right = k + 1, len(numbers) - 1
            expected = target - v

            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return k + 1 ,mid + 1

    def book2(self, numbers, target):
        for k, v in enumerate(numbers):
            expected = target - v
            nums = numbers[k + 1:]
            i = bisect.bisect_left(nums, expected)
            if i < len(nums) and  nums == expected:
                return k + 1, i + k + 2

    def book3(self, numbers, target):
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k + 1)
            if i < len(numbers) and numbers[i] == expected:
                return k + 1, i + 1


                

a = Solution()
print(a.twoSum([2,7,8, 10, 11,15], 18))