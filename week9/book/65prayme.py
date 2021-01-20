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
    answer: int = 0
    def search(self, nums: List[int], target: int) -> int:
        # 정렬이 되어 있는 상태다.
        def binary_search(arr: List[int]):
            middle = len(arr)//2
            self.answer = middle
            if middle == 0:
                # print(arr)
                if arr[0] == target:
                    return self.answer
                return -1

            if arr[middle] == target:
                return self.answer
            elif arr[middle] < target:
                return binary_search(arr[middle:])
            elif arr[middle] > target:
                return binary_search(arr[:middle])

        return binary_search(nums)
    
    def book_recursion(self, nums:List[int], target: int) -> int:
        def binary_search(left, right):
            if left <= right:
                # mid = left + (right - left) // 2 정확한 중앙값을 포기
                mid = (left+right) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid - 1)
                else:
                    return mid

            else:
                return -1
            
        return binary_search(0, len(nums) - 1)

    def book_iter(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1
            
    def book_bisect(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

    def book_index(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1






print(Solution().search([-1,0,3,5,9,12], 9))

